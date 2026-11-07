"""Synthetic repeated-measures eye-tracking analysis demonstration.

This public-safe demo mirrors the portfolio's reasoning about participant-level
quality control and within-person contrasts without using dissertation data or
licensed face stimuli.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)


def generate_trials(n_participants=50, trials_per_participant=90, seed=7):
    rng = np.random.default_rng(seed)
    rows = []
    emotions = np.array(["angry", "happy", "neutral"])
    sounds = np.array(["smartphone", "tone", "silent"])
    for pid in range(n_participants):
        participant_intercept = rng.normal(0, 45)
        pupil_intercept = rng.normal(0, 3)
        combos = [(e, s) for e in emotions for s in sounds]
        reps = int(np.ceil(trials_per_participant / len(combos)))
        design = (combos * reps)[:trials_per_participant]
        rng.shuffle(design)
        for trial, (emotion, sound) in enumerate(design):
            first_fix = 725 + participant_intercept + rng.normal(0, 70)
            first_fix += 24 if emotion == "angry" else (-16 if emotion == "happy" else 0)
            pupil_var = 81.5 + pupil_intercept + rng.normal(0, 6)
            pupil_var += 2.2 if sound == "smartphone" else (-1.5 if sound == "silent" else 0)
            signal_quality = np.clip(rng.normal(0.92, 0.07), 0.45, 1.0)
            # A small participant-specific chance of lower-quality trials.
            if rng.random() < 0.025:
                signal_quality = rng.uniform(0.45, 0.72)
            rows.append({
                "participant_id": pid,
                "trial": trial,
                "emotion": emotion,
                "sound": sound,
                "first_fix_ms": first_fix,
                "pupil_variability": pupil_var,
                "signal_quality": signal_quality,
                "blink": rng.binomial(1, 0.08),
                "rt_ms": 520 + participant_intercept * 0.15 + rng.normal(0, 75) + (12 if emotion == "angry" else 0),
            })
    return pd.DataFrame(rows)


def apply_qc(df, trial_quality_threshold=0.75, participant_usable_fraction=0.75):
    out = df.copy()
    out["trial_usable"] = out.signal_quality >= trial_quality_threshold
    frac = out.groupby("participant_id").trial_usable.mean()
    valid_participants = frac[frac >= participant_usable_fraction].index
    out["participant_usable"] = out.participant_id.isin(valid_participants)
    clean = out[out.trial_usable & out.participant_usable].copy()
    return out, clean, frac


def participant_condition_means(clean, value_col, condition_col):
    return clean.groupby(["participant_id", condition_col])[value_col].mean().unstack(condition_col)


def within_subject_contrasts(clean):
    emo = participant_condition_means(clean, "first_fix_ms", "emotion")
    snd = participant_condition_means(clean, "pupil_variability", "sound")
    emo_pair = emo.dropna(subset=["angry", "happy"])
    snd_pair = snd.dropna(subset=["smartphone", "silent"])
    emo_test = ttest_rel(emo_pair["angry"], emo_pair["happy"])
    snd_test = ttest_rel(snd_pair["smartphone"], snd_pair["silent"])
    return {
        "emotion": {
            "n_participants": int(len(emo_pair)),
            "angry_mean": float(emo_pair.angry.mean()),
            "happy_mean": float(emo_pair.happy.mean()),
            "mean_difference_ms": float((emo_pair.angry - emo_pair.happy).mean()),
            "p_value": float(emo_test.pvalue),
        },
        "sound": {
            "n_participants": int(len(snd_pair)),
            "smartphone_mean": float(snd_pair.smartphone.mean()),
            "silent_mean": float(snd_pair.silent.mean()),
            "mean_difference": float((snd_pair.smartphone - snd_pair.silent).mean()),
            "p_value": float(snd_test.pvalue),
        },
    }


def main():
    df = generate_trials()
    qc, clean, usable_fraction = apply_qc(df)
    contrasts = within_subject_contrasts(clean)

    qc.to_csv(OUT / "synthetic_eye_tracking_trials.csv", index=False)
    usable_fraction.rename("usable_fraction").to_csv(OUT / "synthetic_eye_participant_qc.csv")
    pd.DataFrame([
        {"contrast": "angry_vs_happy_first_fixation", **contrasts["emotion"]},
        {"contrast": "smartphone_vs_silent_pupil_variability", **contrasts["sound"]},
    ]).to_csv(OUT / "synthetic_eye_within_subject_contrasts.csv", index=False)

    emo = participant_condition_means(clean, "first_fix_ms", "emotion").mean().sort_values()
    snd = participant_condition_means(clean, "pupil_variability", "sound").mean().sort_values()

    fig, ax = plt.subplots(figsize=(7, 4.5))
    emo.plot(kind="bar", ax=ax)
    ax.set_ylabel("Participant-averaged first-fixation latency (ms)")
    ax.set_title("Synthetic repeated-measures fixation summary")
    fig.tight_layout()
    fig.savefig(OUT / "eye_first_fixation_summary.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7, 4.5))
    snd.plot(kind="bar", ax=ax)
    ax.set_ylabel("Participant-averaged pupil variability (a.u.)")
    ax.set_title("Synthetic repeated-measures pupil summary")
    fig.tight_layout()
    fig.savefig(OUT / "eye_pupil_variability_summary.png", dpi=160)
    plt.close(fig)

    print(f"Usable participants: {clean.participant_id.nunique()}/{df.participant_id.nunique()}")
    print(f"Usable trials: {len(clean)}/{len(df)}")
    print("Within-subject emotion contrast:", contrasts["emotion"])
    print("Within-subject sound contrast:", contrasts["sound"])


if __name__ == "__main__":
    main()
