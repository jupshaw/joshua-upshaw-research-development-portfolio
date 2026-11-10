# Clinical AI: Oncology Prior-Authorization Workflow Research

**Role:** Principal Investigator, Hidalga Technologies  
**Funding:** NSF SBIR Phase I Award #2507367  
**Evidence status:** Retrospective, non-interventional, single-site technical feasibility research

## Executive readout

**Problem:** Prior-authorization work in community oncology is fragmented across structured EHR data, clinical notes, payer requirements, workflow events, and incomplete outcome histories.  
**Approach:** Build a reproducible retrospective research pipeline spanning clinical-field extraction, denial-risk modeling, workflow timing, rework signals, and operational modeling.  
**Result:** Extraction and denial-risk discrimination met feasibility targets, while incomplete historical action capture prevented causal claims about workflow optimization. That limitation became a prospective telemetry and pilot specification.

## My role

- NSF SBIR Principal Investigator
- Research question, cohort, endpoint, and validation design
- Clinical data curation and model-evaluation leadership
- Cross-functional translation across clinical, engineering, operations, compliance, and executive stakeholders
- Prospective pilot instrumentation and acceptance-criteria design

## Data / study scale

| Measure | Value |
|---|---:|
| Age-eligible patients with PA events | 24,167 |
| Analytic PA case records | 200,513 |
| Free-text clinical notes | 148,703 |
| Resolved cases for prediction | 96,261 |
| Denial prevalence | ~2.4% |

## Methods and technical implementation

Python, pandas, SQL, longitudinal case reconstruction, source reconciliation, clinical NLP, LightGBM, patient-grouped validation, temporal stability analysis, PR-AUC/ROC-AUC, calibration, threshold/workload analysis, workflow timing, simulation, provenance, and prospective telemetry design.

See [methods.md](methods.md) and [public_safe_architecture.md](public_safe_architecture.md).

## Results

| Endpoint | Result |
|---|---:|
| Combined clinical-field extraction | F1 = **0.967** |
| Denial-risk discrimination | ROC-AUC = **0.877** |
| Denial-class PR-AUC | **0.289** vs **0.024** no-skill baseline |
| Sigmoid-calibrated Brier score | **0.052** |
| Expected calibration error | **0.064** |
| Workflow simulation | **15%+ shorter median TAT**, simulated not observed |

See [results.md](results.md) and [METRIC_PROVENANCE.md](METRIC_PROVENANCE.md).

## What changed because of the result

Historical outcomes were more complete than historical staff-action data. Instead of inferring causal workflow effects from incomplete records, the program converted the limitation into a prospective measurement specification: recommendation exposure, action eligibility, action selected, override/reason, timestamps, payer response, workload, and final outcome.

See [prospective_design.md](prospective_design.md).

## Limitations

- Retrospective, single-site feasibility evidence
- Rare denial outcome and operational precision constraints
- Historical actions incompletely captured
- Temporal and workflow changes can alter model performance
- Simulation does not establish real-world intervention effect

## Model governance

- [Model Card](MODEL_CARD.md)
- [Metric Provenance](METRIC_PROVENANCE.md)
- Human review boundaries and prospective deployment gates are explicit

## Reproducibility / public artifacts

No PHI, clinic raw exports, payer-confidential material, or proprietary production code are released. The public synthetic example in [`examples/clinical_ml_validation_demo.py`](../../examples/clinical_ml_validation_demo.py) demonstrates grouped vs temporal validation, explicit calibration, PR-AUC, Brier/ECE, and workload-aware thresholding.

## Analytical visualization and decision support

The [Applied AI Analytics, Visualization & Decision Support report](analytics/REPORT.md) translates publicly summarized retrospective predictive-model and workflow results into executive visualizations and bounded recommendations. A third figure demonstrates hypothetical labor-only sensitivity using openly documented assumptions. See the [reproducible code and figures](analytics/README.md); no individual clinic data or realized financial benefits are presented.
