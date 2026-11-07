# Apply the November 2026 Portfolio Rigor Update

This update was built from the current public portfolio structure after a live GitHub review.

## Replace / add

Copy this package over the repository root. It updates:

- `README.md`
- `START_HERE.md`
- `PROJECTS.md`
- `CHANGELOG.md`
- `.gitignore`
- `.github/workflows/validate.yml`
- `requirements.txt`
- `requirements-lock.txt`
- `assets/evidence_summary.svg`
- `assets/social_preview.png`
- `examples/README.md`
- all three public demo scripts
- all three public notebooks
- flagship project READMEs 01 through 05
- `projects/05_clinical_ai_oncology/MODEL_CARD.md`
- `projects/05_clinical_ai_oncology/METRIC_PROVENANCE.md`
- expanded tests and notebook-execution validation
- `docs/maintainer/PUBLISHING.md`

## Delete / move from the existing repository

Delete the obsolete root file:

```text
UPDATE_MANIFEST.md
```

Replace the root `PUBLISHING.md` with the new:

```text
docs/maintainer/PUBLISHING.md
```

## Validate locally

```bash
python -m pip install -r requirements-lock.txt
python examples/eeg_qc_demo.py
python examples/eye_tracking_metrics_demo.py
python examples/clinical_ml_validation_demo.py
pytest -q
python tests/execute_notebooks.py
```

Expected test result for this package: **7 passed**, followed by successful execution of all 3 notebooks.

## Commit and push

```bash
git add -A
git commit -m "Strengthen portfolio technical rigor and reproducibility"
git switch -c portfolio-rigor-v1.1 # if the update branch does not already exist
git push -u origin portfolio-rigor-v1.1
```

Open a pull request against `main`; do not merge without review.

## Optional GitHub UI steps after review

1. Repository **Settings -> General**: disable Wiki and Projects if you do not plan to use them.
2. Repository **Settings -> General -> Social preview**: upload `assets/social_preview.png`.
3. Create a **v1.1.0** release using the 2026-11-06 changelog entry.
4. Confirm the `validate-portfolio` action passes on the new commit.
