"""Synthetic rare-outcome clinical ML validation demonstration.

The goal is to show why patient grouping, temporal validation, PR-AUC,
calibration, and operational thresholding matter. Metrics are synthetic and
must not be confused with Hidalga study results.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score, average_precision_score, brier_score_loss, precision_recall_curve
from sklearn.model_selection import GroupShuffleSplit
from sklearn.calibration import calibration_curve

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)
RNG = np.random.default_rng(2026)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def make_data(n_patients=6000, min_cases=1, max_cases=5):
    rows = []
    for pid in range(n_patients):
        n = RNG.integers(min_cases, max_cases + 1)
        base_risk = RNG.normal(0, 0.5)
        for j in range(n):
            day = RNG.integers(0, 730)
            x1 = RNG.normal()
            x2 = RNG.normal()
            payer_strictness = RNG.beta(2, 4)
            drift = (day / 730) * 0.8
            logit = -4.25 + 0.9*x1 + 0.6*x2 + 1.1*payer_strictness + base_risk - drift*x1
            p = sigmoid(logit)
            y = RNG.binomial(1, p)
            rows.append((pid, day, x1, x2, payer_strictness, y))
    return pd.DataFrame(rows, columns=["patient_id","day","x1","x2","payer_strictness","denied"])


def fit_eval(train, test, label):
    features = ["x1","x2","payer_strictness"]
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(train[features], train.denied)
    p = model.predict_proba(test[features])[:,1]
    out = {
        "split": label,
        "n_test": len(test),
        "prevalence": test.denied.mean(),
        "roc_auc": roc_auc_score(test.denied, p),
        "pr_auc": average_precision_score(test.denied, p),
        "brier": brier_score_loss(test.denied, p),
    }
    return model, p, out


def threshold_for_recall(y, p, target_recall=0.70):
    precision, recall, thresholds = precision_recall_curve(y, p)
    valid = np.where(recall[:-1] >= target_recall)[0]
    if len(valid) == 0:
        idx = np.argmax(recall[:-1])
    else:
        idx = valid[-1]
    thr = thresholds[idx]
    pred = p >= thr
    tp = ((pred == 1) & (y.to_numpy() == 1)).sum()
    fp = ((pred == 1) & (y.to_numpy() == 0)).sum()
    fn = ((pred == 0) & (y.to_numpy() == 1)).sum()
    return {
        "threshold": float(thr),
        "recall": tp / max(tp + fn, 1),
        "precision": tp / max(tp + fp, 1),
        "flag_rate": pred.mean(),
    }


def main():
    df = make_data()
    features = ["x1","x2","payer_strictness"]

    # Patient-grouped random split.
    splitter = GroupShuffleSplit(n_splits=1, test_size=0.25, random_state=42)
    tr_idx, te_idx = next(splitter.split(df, groups=df.patient_id))
    train_random, test_random = df.iloc[tr_idx], df.iloc[te_idx]
    _, p_random, m_random = fit_eval(train_random, test_random, "patient-grouped random")

    # Forward temporal split, with patient overlap removed to stay conservative.
    cutoff = int(df.day.quantile(0.75))
    train_temp = df[df.day < cutoff].copy()
    test_temp = df[df.day >= cutoff].copy()
    train_patients = set(train_temp.patient_id)
    test_temp = test_temp[~test_temp.patient_id.isin(train_patients)].copy()
    if test_temp.denied.nunique() < 2 or len(test_temp) < 100:
        # Fallback: patient-first temporal split using first observed case date.
        first_day = df.groupby('patient_id').day.min()
        cutoff_pid = first_day.quantile(0.75)
        future_pids = first_day[first_day >= cutoff_pid].index
        past_pids = first_day[first_day < cutoff_pid].index
        train_temp = df[df.patient_id.isin(past_pids)].copy()
        test_temp = df[df.patient_id.isin(future_pids)].copy()
    _, p_temp, m_temp = fit_eval(train_temp, test_temp, "forward temporal")

    metrics = pd.DataFrame([m_random, m_temp])
    metrics.to_csv(OUT / "synthetic_clinical_ml_metrics.csv", index=False)

    workload = threshold_for_recall(test_temp.denied, p_temp, 0.70)
    pd.DataFrame([workload]).to_csv(OUT / "synthetic_threshold_workload.csv", index=False)

    fig, ax = plt.subplots(figsize=(7.5,4.5))
    plot = metrics.set_index("split")[["roc_auc","pr_auc"]]
    plot.plot(kind="bar", ax=ax)
    ax.axhline(test_temp.denied.mean(), linestyle="--", linewidth=1, label="temporal prevalence")
    ax.set_ylim(0,1)
    ax.set_ylabel("Metric")
    ax.set_title("Synthetic random vs temporal validation")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "clinical_ml_validation_summary.png", dpi=160)
    plt.close(fig)

    frac_pos, mean_pred = calibration_curve(test_temp.denied, p_temp, n_bins=8, strategy="quantile")
    fig, ax = plt.subplots(figsize=(5.5,5))
    ax.plot(mean_pred, frac_pos, marker="o", label="synthetic model")
    ax.plot([0,1],[0,1], linestyle="--", label="ideal")
    ax.set_xlabel("Mean predicted probability")
    ax.set_ylabel("Observed event rate")
    ax.set_title("Synthetic calibration curve")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "clinical_ml_calibration.png", dpi=160)
    plt.close(fig)

    print(metrics.to_string(index=False))
    print("Threshold/workload summary:", workload)


if __name__ == "__main__":
    main()
