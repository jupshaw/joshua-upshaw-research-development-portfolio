# Analytical Visualization and Decision Support

A reproducible, public-safe analytics and reporting module linked to the [oncology AI research project](../README.md).

**Review first:** [Applied AI Analytics, Visualization & Decision Support](REPORT.md)

| Analysis | Question | Figure | Evidence |
|---|---|---|---|
| Predictive reliability | Is rare-denial triage promising enough for further evaluation? | [Performance summary](figures/01_predictive_performance.svg) | Previously reported retrospective aggregates |
| Operational analytics | What should a clinic measure or investigate before redesign? | [Workflow priorities](figures/02_workflow_priorities.svg) | Retrospective summaries and derived indices |
| Investment sensitivity | Under what assumptions could avoided administrative effort offset costs? | [Financial sensitivity](figures/03_illustrative_financial_sensitivity.svg) | Fully illustrative assumptions |

## Rebuild

```bash
python -m pip install -r requirements.txt
python projects/05_clinical_ai_oncology/analytics/visualize.py
pytest tests/test_analytics_visualization.py -q
```

Outputs include high-resolution PNGs, vector SVGs, a CSV scenario table, and source notes in [`figures/`](figures/). Reproducible inputs live in [`evidence_and_assumptions.json`](evidence_and_assumptions.json). Analytical logic is in [`visualize.py`](visualize.py), and tests are in [`tests/test_analytics_visualization.py`](../../../tests/test_analytics_visualization.py).

**Evidence guardrails:** This is not production software. No PHI, restricted EHR exports, individual probabilities, actual staff time savings or proprietary payer criteria are included. The financial chart is a transparent hypothetical scenario, not historical or prospective clinic ROI.
