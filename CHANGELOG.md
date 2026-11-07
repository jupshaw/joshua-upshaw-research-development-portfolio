# Changelog

## 1.1.0 - 2026-11-06

- Tightened the README and project index for faster executive and technical review.
- Standardized flagship project READMEs around role, methods, results, decision impact, limitations, and reproducibility.
- Upgraded the EEG demo to include events, QC, epoching, ERP summaries, and spectral summaries.
- Upgraded the eye-tracking demo to repeated participants/trials with participant and trial QC plus within-subject contrasts.
- Upgraded the clinical ML demo with patient-disjoint temporal validation, explicit Platt calibration, ECE, and workload-aware thresholding.
- Added analytical integrity tests, notebook execution, and link checks to CI.
- Added `MODEL_CARD.md` and `METRIC_PROVENANCE.md` for clinical AI governance.
- Added an exact `requirements-lock.txt` environment alongside compatibility requirements.
- Added evidence-summary and social-preview assets.
- Moved publishing guidance to `docs/maintainer/` and removed obsolete update artifacts from the public root.
- During integration, enforced a strict encounter-time cutoff in the synthetic clinical split, labeled test-selected thresholds exploratory, and regenerated synthetic clinical outputs; reported study metrics are unchanged.
- Added the notebook kernel dependency, aligned the NumPy minimum with the EEG API, and expanded link checks to all Markdown pages and embedded assets.

## 1.0.0 - 2026-10-22

- Created executive and technical navigation paths.
- Added five flagship research/R&D case studies.
- Added additional behavioral, affective, and research-assistant projects.
- Added KSA and methods matrices.
- Added synthetic EEG, eye-tracking, and clinical-ML demonstrations.
- Added public-data/IP safeguards and lightweight CI validation.
