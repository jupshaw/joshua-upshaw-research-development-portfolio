"""Synthetic 360-trial eye-tracking analysis demonstration.

This demo mirrors the portfolio's endpoint logic (fixation, pupil, signal quality)
without using dissertation participant data or licensed face stimuli.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)
RNG = np.random.default_rng(7)


def generate_trials(n=360):
    emotions = np.resize(np.array(["angry","happy","neutral"]), n)
    sounds = np.resize(np.array(["smartphone","tone","silent"]), n)
    RNG.shuffle(emotions)
    RNG.shuffle(sounds)
    base_fix = RNG.normal(725, 90, n)
    first_fix_ms = base_fix + np.where(emotions == "angry", 22, np.where(emotions == "happy", -16, 4))
    pupil_var = RNG.normal(81.5, 8, n) + np.where(sounds == "smartphone", 2.2, np.where(sounds == "silent", -1.5, 0))
    signal_quality = np.clip(RNG.normal(0.92, 0.08, n), 0.4, 1.0)
    blink = RNG.binomial(1, 0.08, n)
    rt = RNG.normal(520, 90, n) + np.where(emotions == "angry", 12, 0)
    return pd.DataFrame({
        "emotion": emotions,
        "sound": sounds,
        "first_fix_ms": first_fix_ms,
        "pupil_variability": pupil_var,
        "signal_quality": signal_quality,
        "blink": blink,
        "rt_ms": rt,
    })


def main():
    df = generate_trials()
    df["usable"] = df.signal_quality >= 0.75
    clean = df[df.usable].copy()
    clean.to_csv(OUT / "synthetic_eye_tracking_trials.csv", index=False)

    emo = clean.groupby("emotion")["first_fix_ms"].mean().sort_values()
    snd = clean.groupby("sound")["pupil_variability"].mean().sort_values()

    a = clean.loc[clean.emotion.eq("angry"), "first_fix_ms"]
    h = clean.loc[clean.emotion.eq("happy"), "first_fix_ms"]
    stat1 = ttest_ind(a, h, equal_var=False)
    s = clean.loc[clean.sound.eq("smartphone"), "pupil_variability"]
    z = clean.loc[clean.sound.eq("silent"), "pupil_variability"]
    stat2 = ttest_ind(s, z, equal_var=False)

    fig, ax = plt.subplots(figsize=(7,4.5))
    emo.plot(kind="bar", ax=ax)
    ax.set_ylabel("Mean first-fixation latency (ms)")
    ax.set_title("Synthetic first-fixation summary")
    fig.tight_layout()
    fig.savefig(OUT / "eye_first_fixation_summary.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(7,4.5))
    snd.plot(kind="bar", ax=ax)
    ax.set_ylabel("Mean pupil variability (a.u.)")
    ax.set_title("Synthetic pupil-variability summary")
    fig.tight_layout()
    fig.savefig(OUT / "eye_pupil_variability_summary.png", dpi=160)
    plt.close(fig)

    print(f"Usable trials: {len(clean)}/{len(df)}")
    print("First fixation by emotion:\n", emo)
    print(f"Synthetic angry vs happy Welch t-test p={stat1.pvalue:.4f}")
    print("Pupil variability by sound:\n", snd)
    print(f"Synthetic smartphone vs silent Welch t-test p={stat2.pvalue:.4f}")


if __name__ == "__main__":
    main()
