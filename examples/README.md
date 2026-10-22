# Public Synthetic Demonstrations

These examples are intentionally small, deterministic, and synthetic. They demonstrate analytical reasoning without exposing participant-level research data, protected clinical data, or proprietary production code.

## Included

- `eeg_qc_demo.py` - synthetic multichannel EEG, filtering, artifact flagging, and band-power summary
- `eye_tracking_metrics_demo.py` - synthetic 360-trial gaze/physiology dataset with trial QC and endpoint summaries
- `clinical_ml_validation_demo.py` - rare-outcome classification showing random vs temporal validation, PR-AUC, calibration, and workload-aware thresholds

Corresponding notebooks are in `../notebooks/`.

## Run

```bash
python -m pip install -r ../requirements.txt
python eeg_qc_demo.py
python eye_tracking_metrics_demo.py
python clinical_ml_validation_demo.py
```

Outputs are saved under `examples/outputs/`.
