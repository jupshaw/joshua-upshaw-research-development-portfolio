# Publishing This Repository to GitHub

## Before publishing

1. Review [PUBLIC_DATA_AND_IP_POLICY.md](PUBLIC_DATA_AND_IP_POLICY.md).
2. Confirm that no private, licensed, clinical, or confidential files were added after generation.
3. Replace or add a public resume only if you are comfortable exposing its contact information.
4. Run the validation commands below.

## Local validation

```bash
python -m pip install -r requirements.txt
python examples/eeg_qc_demo.py
python examples/eye_tracking_metrics_demo.py
python examples/clinical_ml_validation_demo.py
pytest -q
```

## Create the repository

```bash
git init
git add .
git commit -m "Initial research and development portfolio"
git branch -M main
git remote add origin https://github.com/<username>/<repository>.git
git push -u origin main
```

Recommended repository name:

```text
joshua-upshaw-research-development-portfolio
```

## Suggested GitHub topics

`clinical-data-science`, `neuroscience`, `eeg`, `eye-tracking`, `fmri`, `machine-learning`, `real-world-evidence`, `healthcare-ai`, `research-portfolio`, `clinical-nlp`

## Presentation recommendations

- Pin the repository to your GitHub profile.
- Put the repository link on LinkedIn and your resume.
- Keep the top-level README concise; move detailed methods into project folders.
- Use GitHub Releases for large portfolio PDFs if repository size becomes an issue.
- Treat every new public clinical example as a privacy/IP review event.
