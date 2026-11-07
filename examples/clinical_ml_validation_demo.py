"""Synthetic rare-outcome clinical ML validation demonstration.

The demo shows patient-group separation, forward temporal validation, explicit
calibration, PR-AUC, Brier score, expected calibration error, and workload-aware
thresholding. Metrics are synthetic and must not be confused with study results.
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


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def logit(p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def make_data(n_patients=6000, min_cases=1, max_cases=5, seed=2026):
    rng = np.random.default_rng(seed)
    rows = []
    for pid in range(n_patients):
        n = int(rng.integers(min_cases, max_cases + 1))
        base_risk = rng.normal(0, 0.5)
        first_day = int(rng.integers(0, 550))
        for j in range(n):
            day = min(first_day + int(rng.integers(0, 181)), 729)
            x1 = rng.normal()
            x2 = rng.normal()
            payer_strictness = rng.beta(2, 4)
            drift = (day / 730) * 0.8
            score = -4.25 + 0.9 * x1 + 0.6 * x2 + 1.1 * payer_strictness + base_risk - drift * x1
            p = sigmoid(score)
            y = rng.binomial(1, p)
            rows.append((pid, day, x1, x2, payer_strictness, y))
    return pd.DataFrame(rows, columns=["patient_id", "day", "x1", "x2", "payer_strictness", "denied"])


def patient_grouped_split(df, test_size=0.25, seed=42):
    splitter = GroupShuffleSplit(n_splits=1, test_size=test_size, random_state=seed)
    tr_idx, te_idx = next(splitter.split(df, groups=df.patient_id))
    return df.iloc[tr_idx].copy(), df.iloc[te_idx].copy()


def forward_patient_split(df, quantile=0.75):
    """Hold out newly arriving patients and exclude post-cutoff training cases."""
    first_day = df.groupby("patient_id").day.min()
    cutoff = float(first_day.quantile(quantile))
    train_pids = first_day[first_day < cutoff].index
    test_pids = first_day[first_day >= cutoff].index
    train = df[df.patient_id.isin(train_pids) & (df.day < cutoff)].copy()
    test = df[df.patient_id.isin(test_pids)].copy()
    return train, test, cutoff


def fit_base_model(train):
    features = ["x1", "x2", "payer_strictness"]
    model = LogisticRegression(max_iter=1000, class_weight="balanced")
    model.fit(train[features], train.denied)
    return model


def predict(model, df):
    features = ["x1", "x2", "payer_strictness"]
    return model.predict_proba(df[features])[:, 1]


def fit_platt_calibrator(y, p):
    calibrator = LogisticRegression(max_iter=1000)
    calibrator.fit(logit(p).reshape(-1, 1), np.asarray(y))
    return calibrator


def apply_platt(calibrator, p):
    return calibrator.predict_proba(logit(p).reshape(-1, 1))[:, 1]


def expected_calibration_error(y, p, n_bins=10):
    y = np.asarray(y)
    p = np.asarray(p)
    edges = np.linspace(0, 1, n_bins + 1)
    total = len(y)
    ece = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        take = (p >= lo) & (p < hi if hi < 1 else p <= hi)
        if take.any():
            ece += take.mean() * abs(y[take].mean() - p[take].mean())
    return float(ece)


def metric_row(y, p, label):
    return {
        "split": label,
        "n_test": int(len(y)),
        "prevalence": float(np.mean(y)),
        "roc_auc": float(roc_auc_score(y, p)),
        "pr_auc": float(average_precision_score(y, p)),
        "brier": float(brier_score_loss(y, p)),
        "ece": expected_calibration_error(y, p),
    }


def threshold_for_recall(y, p, target_recall=0.70):
    precision, recall, thresholds = precision_recall_curve(y, p)
    valid = np.where(recall[:-1] >= target_recall)[0]
    idx = valid[-1] if len(valid) else int(np.argmax(recall[:-1]))
    thr = float(thresholds[idx])
    pred = p >= thr
    y = np.asarray(y)
    tp = int(((pred == 1) & (y == 1)).sum())
    fp = int(((pred == 1) & (y == 0)).sum())
    fn = int(((pred == 0) & (y == 1)).sum())
    return {
        "threshold": thr,
        "recall": tp / max(tp + fn, 1),
        "precision": tp / max(tp + fp, 1),
        "flag_rate": float(pred.mean()),
        "flags_per_1000": float(pred.mean() * 1000),
    }


def evaluate_grouped(df):
    train, test = patient_grouped_split(df)
    fit, calib = patient_grouped_split(train, test_size=0.20, seed=17)
    model = fit_base_model(fit)
    p_calib_base = predict(model, calib)
    calibrator = fit_platt_calibrator(calib.denied, p_calib_base)
    p_test_base = predict(model, test)
    p_test_cal = apply_platt(calibrator, p_test_base)
    return train, test, p_test_base, p_test_cal


def evaluate_temporal(df):
    train, test, cutoff = forward_patient_split(df)
    fit, calib = patient_grouped_split(train, test_size=0.20, seed=19)
    model = fit_base_model(fit)
    p_calib_base = predict(model, calib)
    calibrator = fit_platt_calibrator(calib.denied, p_calib_base)
    p_test_base = predict(model, test)
    p_test_cal = apply_platt(calibrator, p_test_base)
    return train, test, p_test_base, p_test_cal, cutoff


def main():
    df = make_data()
    _, grouped_test, gp_base, gp_cal = evaluate_grouped(df)
    temp_train, temp_test, tp_base, tp_cal, cutoff = evaluate_temporal(df)

    metrics = pd.DataFrame([
        metric_row(grouped_test.denied, gp_base, "patient-grouped uncalibrated"),
        metric_row(grouped_test.denied, gp_cal, "patient-grouped calibrated"),
        metric_row(temp_test.denied, tp_base, "forward temporal uncalibrated"),
        metric_row(temp_test.denied, tp_cal, "forward temporal calibrated"),
    ])
    metrics.to_csv(OUT / "synthetic_clinical_ml_metrics.csv", index=False)

    workload = threshold_for_recall(temp_test.denied, tp_cal, 0.70)
    pd.DataFrame([workload]).to_csv(OUT / "synthetic_threshold_workload.csv", index=False)

    fig, ax = plt.subplots(figsize=(8.5, 4.8))
    plot = metrics.set_index("split")[["roc_auc", "pr_auc"]]
    plot.plot(kind="bar", ax=ax)
    ax.axhline(temp_test.denied.mean(), linestyle="--", linewidth=1, label="temporal prevalence")
    ax.set_ylim(0, 1)
    ax.set_ylabel("Metric")
    ax.set_title("Synthetic grouped vs temporal validation")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "clinical_ml_validation_summary.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(5.8, 5.2))
    for label, p in [("uncalibrated", tp_base), ("Platt calibrated", tp_cal)]:
        frac_pos, mean_pred = calibration_curve(temp_test.denied, p, n_bins=8, strategy="quantile")
        ax.plot(mean_pred, frac_pos, marker="o", label=label)
    ax.plot([0, 1], [0, 1], linestyle="--", label="ideal")
    ax.set_xlabel("Mean predicted probability")
    ax.set_ylabel("Observed event rate")
    ax.set_title("Synthetic temporal calibration")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "clinical_ml_calibration.png", dpi=160)
    plt.close(fig)

    print(metrics.to_string(index=False))
    print(f"Temporal split patient cutoff day: {cutoff:.1f}")
    print(f"Patient overlap train/test: {len(set(temp_train.patient_id) & set(temp_test.patient_id))}")
    print("Exploratory threshold/workload summary (selected on temporal test outcomes):", workload)


if __name__ == "__main__":
    main()
