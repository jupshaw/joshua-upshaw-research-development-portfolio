# Metric Provenance

This page makes the clinical AI results traceable by separating **observed retrospective performance**, **simulation**, and **prospective targets**. Values below reflect the portfolio evidence set currently reported in this repository and should be updated whenever the locked analysis cohort or validation specification changes.

| Metric / claim | Cohort or analysis set | Validation / comparison | Reported value | Evidence status |
|---|---|---|---:|---|
| Clinical-field extraction F1 | Confirmatory structured + free-text field set | Held-out confirmatory evaluation | **0.967** | Retrospective observed |
| Denial-risk ROC-AUC | 96,261 resolved PA cases | Patient-grouped retrospective evaluation | **0.877** | Retrospective observed |
| Denial-class PR-AUC | Same resolved-case analysis | Patient-grouped retrospective evaluation | **0.289** | Retrospective observed |
| No-skill PR baseline | Same resolved-case analysis | Denial prevalence baseline | **0.024** | Derived baseline |
| Sigmoid-calibrated Brier score | Same prediction analysis | Calibration evaluation | **0.052** | Retrospective observed |
| Expected calibration error | Same prediction analysis | Calibration evaluation | **0.064** | Retrospective observed |
| Workflow TAT improvement | Retrospective workflow simulation | Modeled routing policy | **15%+ shorter median TAT** | Simulated, not observed |
| Prospective chart-search / review target | Planned pilot | Prespecified comparator | **>=20% reduction** | Prospective target, not yet demonstrated |

## Interpretation rules

1. **Retrospective discrimination is not prospective utility.** ROC-AUC and PR-AUC quantify ranking performance under the specified historical evaluation design.
2. **Calibration is separate from discrimination.** Probability quality is evaluated independently from ranking quality.
3. **Simulation is not intervention evidence.** The workflow TAT result is retained as a design signal, not as a demonstrated clinic effect.
4. **Prospective targets are not results.** Pilot thresholds describe what the next study must test.
5. **Denominators are versioned.** If a later evidence lock changes cohort counts or validation specifications, this page should change with the corresponding analysis artifact and report.
6. **Base simulation and sensitivity models are distinct.** The approximately 15% base workflow simulation result is not a sensitivity-model result. Separate sensitivity scenarios require their own assumptions, denominators, and provenance and must not replace or be pooled with this base result.

## Why this file exists

Clinical and operational datasets evolve as data-quality rules, cohort definitions, labels, and temporal eligibility criteria are refined. Recording metric provenance prevents valid results from different analysis versions from being collapsed into a single context-free number.
