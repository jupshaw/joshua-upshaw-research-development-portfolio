# Model Card: Denial-Risk Review Triage

## Model purpose

Prioritize prior-authorization cases for **additional human review** when historical patterns suggest elevated denial risk.

## Intended use

- Staff review prioritization
- Research and silent evaluation
- Prospective workflow testing with human oversight

## Not intended for

- Autonomous approval or denial decisions
- Medical-necessity determinations
- Replacement of clinician or utilization-management judgment
- Unsupervised payer submission decisions

## Population and data context

Retrospective oncology prior-authorization records reconstructed from heterogeneous clinical, administrative, payer, and workflow sources. The current portfolio reports **96,261 resolved cases** in the prediction analysis and a denial prevalence of approximately **2.4%**.

## Features and availability

Only information expected to be available before the prediction decision point should be eligible. Feature-availability review is treated as a first-class control because historical datasets can contain information that would not exist in real time.

## Evaluation strategy

- Patient-grouped validation
- Rare-outcome evaluation using PR-AUC alongside ROC-AUC
- Calibration analysis
- Threshold-to-workload translation
- Temporal stability checks
- Leakage review
- Subgroup / sensitivity analysis where data support it

## Reported retrospective performance

| Metric | Value |
|---|---:|
| ROC-AUC | **0.877** |
| Denial-class PR-AUC | **0.289** |
| No-skill PR baseline | **0.024** |
| Sigmoid-calibrated Brier score | **0.052** |
| Expected calibration error | **0.064** |

See [METRIC_PROVENANCE.md](METRIC_PROVENANCE.md) for denominator and evidence-status context.

## Known limitations

- Rare outcome prevalence makes precision operationally important even when ROC-AUC is strong.
- Historical labels and workflow events may be incomplete or inconsistently recorded.
- Performance can degrade as payer policies, clinic workflows, documentation, or patient mix change.
- Retrospective performance does not establish that acting on a prediction improves outcomes.
- Model outputs require prospective evaluation in the workflow where they will be used.

## Human oversight

The model is designed to **surface cases for review**, not determine disposition. Missing, conflicting, or uncertain evidence should trigger review or abstention rather than automated clinical inference.

## Monitoring and prospective evidence required

- Model exposure and timestamp
- Staff action and override / reason
- Feature availability at prediction time
- Payer response and outcome
- Staff workload
- Precision / recall under deployed thresholds
- Calibration and drift
- Subgroup stability
- Time-to-submit, rework, P2P, denial, and reimbursement outcomes

## Deployment gate

A deployment decision should require more than retrospective discrimination. It should require prospective evidence that the model is usable, calibrated, operationally feasible, and beneficial without unacceptable error or workload burden.
