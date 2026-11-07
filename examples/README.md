# Public Synthetic Demonstrations

These examples are deterministic and public-safe. They demonstrate analytical reasoning without exposing participant-level research data, PHI, partner-owned clinical data, or proprietary production code.

| Demo | What it now demonstrates |
|---|---|
| `eeg_qc_demo.py` | Continuous multichannel EEG, event markers, filtering, robust artifact flags, epoching, condition-level ERP summaries, theta/alpha/beta power |
| `eye_tracking_metrics_demo.py` | Repeated participants and trials, trial QC, participant QC, participant-level condition means, within-subject contrasts |
| `clinical_ml_validation_demo.py` | Patient-group separation, forward temporal testing, explicit Platt calibration, ROC/PR-AUC, Brier, ECE, workload-aware thresholds |

Corresponding notebooks are in `../notebooks/`.

## Run

```bash
python -m pip install -r requirements.txt
python examples/eeg_qc_demo.py
python examples/eye_tracking_metrics_demo.py
python examples/clinical_ml_validation_demo.py
pytest -q
python tests/execute_notebooks.py
```

For exact reproduction of the validated environment, use `requirements-lock.txt`.

Outputs are written to `examples/outputs/`.

The temporal clinical split holds out newly arriving patients and removes all
training encounters on or after the cutoff. Base-model fitting and calibration
use disjoint subsets of the remaining training patients. Synthetic clinical
outputs were regenerated after enforcing this strict time boundary; reported
retrospective study metrics are unchanged.

The workload threshold is selected using temporal test outcomes to illustrate
the recall/workload tradeoff. It is exploratory, not an independently validated
operating threshold; prospective use requires selection on development data and
evaluation on an untouched test set.
