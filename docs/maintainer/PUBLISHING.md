# Publishing and Maintenance

## Before a public release

1. Review `PUBLIC_DATA_AND_IP_POLICY.md`.
2. Confirm no PHI, restricted participant-level data, proprietary payer criteria, credentials, licensed stimuli, or production code were added.
3. Run the exact validation environment when possible:

```bash
python -m pip install -r requirements-lock.txt
python examples/eeg_qc_demo.py
python examples/eye_tracking_metrics_demo.py
python examples/clinical_ml_validation_demo.py
pytest -q
python tests/execute_notebooks.py
```

4. Review `projects/05_clinical_ai_oncology/METRIC_PROVENANCE.md` whenever a clinical analysis version changes.
5. Update `CHANGELOG.md` before a tagged release.

## Release discipline

Use a semantic portfolio release such as `v1.0.0` for a major public checkpoint. The release notes should summarize substantive changes to evidence, methods, demonstrations, or public artifacts rather than cosmetic edits.
