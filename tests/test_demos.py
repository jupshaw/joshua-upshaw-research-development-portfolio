import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_eeg_generation_shape():
    mod = load(ROOT / "examples" / "eeg_qc_demo.py")
    t, data = mod.generate_synthetic_eeg(n_channels=8, fs=128, seconds=2)
    assert data.shape == (8, 256)
    assert len(t) == 256


def test_eye_trial_count():
    mod = load(ROOT / "examples" / "eye_tracking_metrics_demo.py")
    df = mod.generate_trials(360)
    assert len(df) == 360
    assert set(df.emotion.unique()) <= {"angry", "happy", "neutral"}


def test_clinical_data_contains_rare_outcome():
    mod = load(ROOT / "examples" / "clinical_ml_validation_demo.py")
    df = mod.make_data(n_patients=1000)
    assert 0 < df.denied.mean() < 0.20
