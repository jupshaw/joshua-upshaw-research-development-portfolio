"""Tests for public summary figures and illustrative sensitivity calculations."""
import importlib.util
import json
from pathlib import Path

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'projects/05_clinical_ai_oncology/analytics/visualize.py'
spec = importlib.util.spec_from_file_location('public_analytics', SCRIPT)
analytics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(analytics)


def test_research_aggregates_and_source_contract():
    data = analytics.load_evidence()
    metrics = data['retrospective_aggregates']
    assert metrics['resolved_cases'] == 96261
    assert metrics['denial_prevalence'] == pytest.approx(0.024)
    assert metrics['denial_pr_auc'] == pytest.approx(0.289)
    assert 'portfolio' not in data['source']['repository_document'].lower() or data['source']['repository_document'].endswith('.md')


def test_rejects_invalid_metric_and_financial_inputs(tmp_path):
    data = analytics.load_evidence()
    data['retrospective_aggregates']['denial_pr_auc'] = 1.2
    src = tmp_path / 'bad.json'
    src.write_text(json.dumps(data), encoding='utf-8')
    with pytest.raises(ValueError):
        analytics.load_evidence(src)
    with pytest.raises(ValueError):
        analytics.modeled_net_benefit(100, 45, 1.2, 500)


def test_illustrative_financial_calculation():
    assert analytics.modeled_net_benefit(2400, 45, 0.25, 120000) == pytest.approx(204000)
    assert analytics.modeled_net_benefit(2400, 35, 0.10, 120000) == pytest.approx(-19200)
    table = analytics.sensitivity_table(analytics.load_evidence()['illustrative_financial_sensitivity'])
    assert len(table) == 9
    assert table['annual_net_value_usd'].min() == pytest.approx(-19200)


def test_generated_figures_and_csv(tmp_path):
    assert len(analytics.build(tmp_path)) == 3
    for filename in ('01_predictive_performance', '02_workflow_priorities',
                     '03_illustrative_financial_sensitivity'):
        assert (tmp_path / f'{filename}.png').stat().st_size > 10000
        assert (tmp_path / f'{filename}.svg').stat().st_size > 10000
    data = pd.read_csv(tmp_path / 'illustrative_sensitivity_table.csv')
    assert data.shape == (9, 3)
    assert (tmp_path / 'SOURCE_NOTES.md').exists()
