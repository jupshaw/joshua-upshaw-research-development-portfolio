import importlib.util
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_eeg_event_epoching_and_reproducibility():
    mod = load(ROOT / "examples" / "eeg_qc_demo.py")
    _, data1, events1 = mod.generate_synthetic_eeg(n_channels=8, fs=128, seconds=40, n_events=20, seed=11)
    _, data2, events2 = mod.generate_synthetic_eeg(n_channels=8, fs=128, seconds=40, n_events=20, seed=11)
    assert np.allclose(data1, data2)
    assert events1.equals(events2)
    clean, mask = mod.preprocess(data1, 128)
    epochs, metadata, epoch_times = mod.epoch_data(clean, mask, events1, 128)
    assert epochs.shape[0] == len(metadata) == 20
    assert epochs.shape[1] == 8
    assert len(epoch_times) == epochs.shape[2]
    assert mask.mean() > 0
    assert metadata.usable.sum() > 0


def test_eeg_bandpower_positive():
    mod = load(ROOT / "examples" / "eeg_qc_demo.py")
    _, data, _ = mod.generate_synthetic_eeg(n_channels=4, fs=128, seconds=20, n_events=8, seed=12)
    clean, _ = mod.preprocess(data, 128)
    frontal = clean.mean(axis=0)
    assert mod.bandpower(frontal, 128, 4, 8) > 0
    assert mod.bandpower(frontal, 128, 8, 13) > 0


def test_eye_tracking_repeated_measures_and_qc():
    mod = load(ROOT / "examples" / "eye_tracking_metrics_demo.py")
    df = mod.generate_trials(n_participants=12, trials_per_participant=36, seed=4)
    assert df.participant_id.nunique() == 12
    assert len(df) == 432
    qc, clean, frac = mod.apply_qc(df)
    assert qc.trial_usable.dtype == bool
    assert 0 < len(clean) <= len(df)
    assert frac.between(0, 1).all()
    results = mod.within_subject_contrasts(clean)
    assert results["emotion"]["n_participants"] > 0
    assert np.isfinite(results["emotion"]["mean_difference_ms"])


def test_clinical_temporal_split_has_no_patient_overlap():
    mod = load(ROOT / "examples" / "clinical_ml_validation_demo.py")
    df = mod.make_data(n_patients=1500, seed=33)
    train, test, cutoff = mod.forward_patient_split(df)
    assert set(train.patient_id).isdisjoint(set(test.patient_id))
    assert train.day.max() < cutoff <= test.day.min()
    assert 0 < test.denied.mean() < 0.20


def test_clinical_calibration_and_threshold_are_well_formed():
    mod = load(ROOT / "examples" / "clinical_ml_validation_demo.py")
    df = mod.make_data(n_patients=1800, seed=34)
    _, test, p_base, p_cal, _ = mod.evaluate_temporal(df)
    assert np.all((p_base >= 0) & (p_base <= 1))
    assert np.all((p_cal >= 0) & (p_cal <= 1))
    assert mod.expected_calibration_error(test.denied, p_cal) >= 0
    workload = mod.threshold_for_recall(test.denied, p_cal, target_recall=0.70)
    assert workload["recall"] >= 0.68
    assert 0 <= workload["flag_rate"] <= 1
    assert workload["flags_per_1000"] >= 0
