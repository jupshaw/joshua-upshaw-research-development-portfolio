# Clinical AI: Oncology Prior-Authorization Workflow Research

**Role:** Principal Investigator, Hidalga Technologies  
**Funding:** NSF SBIR Phase I Award #2507367  
**Evidence status:** Retrospective, non-interventional, single-site technical feasibility research

## Executive readout

**Problem:** Prior-authorization work in community oncology is fragmented across structured EHR data, clinical notes, payer requirements, workflow events, and incomplete outcome histories.  
**Approach:** Build a reproducible retrospective research pipeline spanning clinical-field extraction, denial-risk modeling, workflow timing, rework signals, and operational modeling.  
**Result:** Extraction and denial-risk discrimination met prespecified feasibility targets, while incomplete historical action capture prevented causal claims about workflow optimization. That limitation was converted into a prospective telemetry and pilot specification.

## Study scale

| Measure | Value |
|---|---:|
| Age-eligible patients with PA events | 24,167 |
| Analytic PA case records | 200,513 |
| Free-text clinical notes | 148,703 |
| Resolved cases for prediction | 96,261 |
| Denial prevalence | ~2.4% |

## Selected results

| Endpoint | Result |
|---|---:|
| Combined clinical-field extraction | F1 = **0.967** |
| Denial-risk discrimination | ROC-AUC = **0.877** |
| Denial-class PR-AUC | **0.289** vs **0.024** no-skill baseline |
| Sigmoid-calibrated Brier score | **0.052** |
| Expected calibration error | **0.064** |
| Strict vs lenient payer TAT | **86.1% longer** in reported comparison |
| Workflow simulation | **15%+ shorter median TAT**, simulated not observed |

## Technical stack

Python, pandas, SQL, scikit-learn, LightGBM, rare-outcome evaluation, patient-grouped validation, calibration, longitudinal case reconstruction, clinical NLP, source provenance, clinical terminology normalization, Azure-based healthcare AI infrastructure.

See [methods.md](methods.md), [results.md](results.md), [prospective_design.md](prospective_design.md), and [public_safe_architecture.md](public_safe_architecture.md).
