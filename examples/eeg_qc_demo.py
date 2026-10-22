"""Synthetic EEG quality-control and band-power demonstration.

This is NOT the original publication pipeline. It is a public-safe, deterministic
example showing the analytical concepts used in the portfolio: event-aware signal
processing, artifact flagging, and theta/alpha/beta summaries.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)
RNG = np.random.default_rng(42)


def generate_synthetic_eeg(n_channels=32, fs=256, seconds=20):
    t = np.arange(fs * seconds) / fs
    data = []
    for ch in range(n_channels):
        theta = 2.0 * np.sin(2 * np.pi * 6 * t + RNG.uniform(0, 2*np.pi))
        alpha = 3.0 * np.sin(2 * np.pi * 10 * t + RNG.uniform(0, 2*np.pi))
        beta = 1.0 * np.sin(2 * np.pi * 20 * t + RNG.uniform(0, 2*np.pi))
        noise = RNG.normal(0, 1.5, len(t))
        x = theta + alpha + beta + noise
        data.append(x)
    data = np.vstack(data)
    # Inject a blink-like frontal artifact and brief broadband movement artifact.
    blink = 25 * np.exp(-0.5 * ((t - 5.0) / 0.12) ** 2)
    data[0:4] += blink
    # Place a brief movement artifact only when the requested recording is long enough.
    movement_start = min(12 * fs, max(0, data.shape[1] - 30))
    movement_len = min(30, data.shape[1] - movement_start)
    if movement_len > 0:
        data[:, movement_start:movement_start+movement_len] += RNG.normal(0, 18, (n_channels, movement_len))
    return t, data


def preprocess(data, fs):
    # Minimal public demonstration, not ASR/ICA/ICLabel.
    b, a = signal.butter(4, [1, 35], btype="bandpass", fs=fs)
    filt = signal.filtfilt(b, a, data, axis=1)
    # Robust amplitude gate using per-channel median absolute deviation.
    med = np.median(filt, axis=1, keepdims=True)
    mad = np.median(np.abs(filt - med), axis=1, keepdims=True) + 1e-8
    robust_z = 0.6745 * (filt - med) / mad
    artifact_mask = np.abs(robust_z) > 8
    return filt, artifact_mask


def bandpower(x, fs, lo, hi):
    f, pxx = signal.welch(x, fs=fs, nperseg=fs*2)
    keep = (f >= lo) & (f < hi)
    return np.trapezoid(pxx[keep], f[keep])


def main():
    fs = 256
    t, raw = generate_synthetic_eeg(fs=fs)
    clean, mask = preprocess(raw, fs)
    frontal = clean[:4].mean(axis=0)
    rows = []
    for name, lo, hi in [("theta",4,8),("alpha",8,13),("beta",13,30)]:
        rows.append({"band":name,"power":bandpower(frontal,fs,lo,hi)})
    summary = pd.DataFrame(rows)
    summary["theta_beta_ratio"] = np.nan
    summary.loc[summary.band.eq("theta"), "theta_beta_ratio"] = (
        summary.loc[summary.band.eq("theta"), "power"].iloc[0] /
        summary.loc[summary.band.eq("beta"), "power"].iloc[0]
    )
    summary.to_csv(OUT / "eeg_bandpower_summary.csv", index=False)

    f, pxx = signal.welch(frontal, fs=fs, nperseg=fs*2)
    fig, ax = plt.subplots(figsize=(8,4.5))
    ax.plot(f, pxx)
    ax.set_xlim(1, 35)
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Power spectral density")
    ax.set_title("Synthetic EEG spectral summary")
    fig.tight_layout()
    fig.savefig(OUT / "eeg_spectral_summary.png", dpi=160)
    plt.close(fig)

    artifact_pct = mask.mean() * 100
    print(summary.to_string(index=False))
    print(f"Artifact-flagged sample proportion: {artifact_pct:.2f}%")


if __name__ == "__main__":
    main()
