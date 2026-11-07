"""Synthetic event-based EEG quality-control demonstration.

This is not the original publication pipeline. It is a deterministic, public-safe
example showing concepts used in the portfolio: continuous multichannel EEG,
event markers, band-pass filtering, artifact flagging, stimulus-locked epoching,
condition-level ERP summaries, and theta/alpha/beta power.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

OUT = Path(__file__).resolve().parent / "outputs"
OUT.mkdir(exist_ok=True)


def generate_synthetic_eeg(n_channels=32, fs=256, seconds=120, n_events=60, seed=42):
    rng = np.random.default_rng(seed)
    n_samples = fs * seconds
    t = np.arange(n_samples) / fs
    data = np.empty((n_channels, n_samples), dtype=float)
    for ch in range(n_channels):
        phase = rng.uniform(0, 2 * np.pi, 3)
        data[ch] = (
            2.0 * np.sin(2 * np.pi * 6 * t + phase[0])
            + 3.0 * np.sin(2 * np.pi * 10 * t + phase[1])
            + 1.0 * np.sin(2 * np.pi * 20 * t + phase[2])
            + rng.normal(0, 1.5, n_samples)
        )

    # Space events away from boundaries to support -0.2 to +0.8 s epochs.
    event_times = np.linspace(2.0, seconds - 2.0, n_events)
    conditions = np.where(np.arange(n_events) % 2 == 0, "notification", "control")
    trial_type = np.where(np.arange(n_events) % 5 == 0, "rare", "frequent")

    # Inject small condition-specific event-locked effects in frontal channels.
    for et, cond, kind in zip(event_times, conditions, trial_type):
        center = int(et * fs)
        win = np.arange(-int(0.15 * fs), int(0.45 * fs))
        idx = center + win
        valid = (idx >= 0) & (idx < n_samples)
        tau = win[valid] / fs
        # N2-like negative deflection around 250 ms, larger for notification and rare events.
        amp = -2.2 - (0.8 if cond == "notification" else 0.0) - (0.6 if kind == "rare" else 0.0)
        erp = amp * np.exp(-0.5 * ((tau - 0.25) / 0.055) ** 2)
        data[:4, idx[valid]] += erp
        # Modest event-related theta burst.
        theta = (0.8 + (0.3 if kind == "rare" else 0.0)) * np.sin(2 * np.pi * 6 * tau)
        theta *= np.exp(-0.5 * ((tau - 0.30) / 0.18) ** 2)
        data[:4, idx[valid]] += theta

    # Inject artifacts that QC should detect.
    blink_center = min(25.0, max(2.0, seconds * 0.40))
    blink = 25 * np.exp(-0.5 * ((t - blink_center) / 0.12) ** 2)
    data[:4] += blink
    movement_start = min(int(72 * fs), max(0, n_samples - 45))
    movement_len = min(40, n_samples - movement_start)
    if movement_len > 0:
        data[:, movement_start:movement_start + movement_len] += rng.normal(0, 18, (n_channels, movement_len))

    events = pd.DataFrame({
        "event_time_s": event_times,
        "sample": (event_times * fs).astype(int),
        "condition": conditions,
        "trial_type": trial_type,
    })
    return t, data, events


def preprocess(data, fs):
    b, a = signal.butter(4, [1, 35], btype="bandpass", fs=fs)
    filt = signal.filtfilt(b, a, data, axis=1)
    med = np.median(filt, axis=1, keepdims=True)
    mad = np.median(np.abs(filt - med), axis=1, keepdims=True) + 1e-8
    robust_z = 0.6745 * (filt - med) / mad
    artifact_mask = np.abs(robust_z) > 8
    return filt, artifact_mask


def epoch_data(data, artifact_mask, events, fs, tmin=-0.2, tmax=0.8, artifact_fraction_limit=0.05):
    start = int(round(tmin * fs))
    stop = int(round(tmax * fs))
    offsets = np.arange(start, stop)
    rows = []
    epochs = []
    for i, ev in events.iterrows():
        idx = ev["sample"] + offsets
        if idx.min() < 0 or idx.max() >= data.shape[1]:
            continue
        epoch = data[:, idx]
        mask = artifact_mask[:, idx]
        artifact_fraction = float(mask.mean())
        usable = artifact_fraction <= artifact_fraction_limit
        rows.append({
            "event_id": int(i),
            "condition": ev["condition"],
            "trial_type": ev["trial_type"],
            "artifact_fraction": artifact_fraction,
            "usable": usable,
        })
        epochs.append(epoch)
    return np.stack(epochs), pd.DataFrame(rows), offsets / fs


def bandpower(x, fs, lo, hi):
    f, pxx = signal.welch(x, fs=fs, nperseg=min(fs * 2, x.shape[-1]))
    keep = (f >= lo) & (f < hi)
    return float(np.trapezoid(pxx[keep], f[keep]))


def summarize_epochs(epochs, metadata, epoch_times, fs):
    usable_idx = metadata.index[metadata.usable].to_numpy()
    usable = epochs[usable_idx]
    meta = metadata.loc[usable_idx].reset_index(drop=True)
    frontal = usable[:, :4, :].mean(axis=1)

    # ERP mean amplitude in an N2-like 200-320 ms window.
    n2_mask = (epoch_times >= 0.20) & (epoch_times <= 0.32)
    erp_rows = []
    spec_rows = []
    for cond in ["control", "notification"]:
        take = meta.condition.eq(cond).to_numpy()
        cond_epochs = frontal[take]
        erp_rows.append({
            "condition": cond,
            "n_epochs": int(take.sum()),
            "n2_mean_amplitude": float(cond_epochs[:, n2_mask].mean()),
        })
        flattened = cond_epochs.reshape(-1)
        powers = {name: bandpower(flattened, fs, lo, hi) for name, lo, hi in [
            ("theta", 4, 8), ("alpha", 8, 13), ("beta", 13, 30)
        ]}
        spec_rows.append({
            "condition": cond,
            **powers,
            "theta_beta_ratio": powers["theta"] / max(powers["beta"], 1e-12),
        })
    return pd.DataFrame(erp_rows), pd.DataFrame(spec_rows), frontal, meta


def main():
    fs = 256
    t, raw, events = generate_synthetic_eeg(fs=fs)
    clean, mask = preprocess(raw, fs)
    epochs, metadata, epoch_times = epoch_data(clean, mask, events, fs)
    erp, spectral, frontal_epochs, usable_meta = summarize_epochs(epochs, metadata, epoch_times, fs)

    events.to_csv(OUT / "synthetic_eeg_events.csv", index=False)
    metadata.to_csv(OUT / "synthetic_eeg_epoch_qc.csv", index=False)
    erp.to_csv(OUT / "synthetic_eeg_erp_summary.csv", index=False)
    spectral.to_csv(OUT / "synthetic_eeg_bandpower_summary.csv", index=False)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    for cond in ["control", "notification"]:
        take = usable_meta.condition.eq(cond).to_numpy()
        ax.plot(epoch_times, frontal_epochs[take].mean(axis=0), label=cond)
    ax.axvline(0, linestyle="--", linewidth=1)
    ax.set_xlabel("Time from event (s)")
    ax.set_ylabel("Synthetic frontal amplitude (a.u.)")
    ax.set_title("Synthetic event-locked EEG summary")
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "eeg_event_locked_summary.png", dpi=160)
    plt.close(fig)

    artifact_pct = mask.mean() * 100
    print(erp.to_string(index=False))
    print(spectral.to_string(index=False))
    print(f"Usable epochs: {metadata.usable.sum()}/{len(metadata)}")
    print(f"Artifact-flagged sample proportion: {artifact_pct:.2f}%")


if __name__ == "__main__":
    main()
