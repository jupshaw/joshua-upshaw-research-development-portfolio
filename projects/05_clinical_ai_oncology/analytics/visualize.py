"""Rebuild the public, aggregate-only oncology analytics figures.

Figures A and B show values already present in portfolio summaries. Figure C
is an explicitly illustrative financial sensitivity example. No PHI, predicted
probabilities, confidential source reports, or unpublished patient records.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
NAVY = '#183153'
BLUE = '#2666A2'
TEAL = '#247E90'
PALE = '#E9F1F6'
INK = '#1F3346'
MUTED = '#526779'


def load_evidence(path: Path = HERE / 'evidence_and_assumptions.json') -> dict:
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    metrics = data['retrospective_aggregates']
    for key in ('denial_prevalence', 'denial_pr_auc', 'denial_roc_auc',
                'extraction_mean_f1', 'fully_ready_fraction'):
        value = metrics[key]
        if not isinstance(value, (int, float)) or not np.isfinite(value) or not 0 <= value <= 1:
            raise ValueError(f'{key} must be a finite fraction in [0, 1]')
    if metrics['denial_pr_auc'] < metrics['denial_prevalence']:
        raise ValueError('PR-AUC below baseline, review metric sources before charting')
    if metrics['resolved_cases'] <= 0 or metrics['strict_policy_tat_percent_longer'] < 0:
        raise ValueError('Invalid research denominator or TAT comparison')
    a = data['illustrative_financial_sensitivity']
    if (a['baseline_review_hours_per_month'] <= 0 or a['annual_program_cost_usd'] < 0
            or a['months'] <= 0 or any(rate <= 0 for rate in a['loaded_hourly_cost_usd'])
            or any(not 0 <= f <= 1 for f in a['avoidable_effort_fraction'])):
        raise ValueError('Invalid illustrative financial assumptions')
    return data


def modeled_net_benefit(hours_per_month: float, hourly_rate: float,
                        reduction_fraction: float, annual_cost: float, months: int = 12) -> float:
    """Annual labor-only net value under explicit illustrative assumptions."""
    if hours_per_month < 0 or hourly_rate < 0 or not 0 <= reduction_fraction <= 1 or annual_cost < 0 or months <= 0:
        raise ValueError('Invalid benefit-model parameters')
    return hours_per_month * months * hourly_rate * reduction_fraction - annual_cost


def sensitivity_table(assumptions: dict) -> pd.DataFrame:
    rows = []
    for rate in assumptions['loaded_hourly_cost_usd']:
        for frac in assumptions['avoidable_effort_fraction']:
            rows.append({'loaded_hourly_cost_usd': rate, 'avoidable_effort_pct': int(frac * 100),
                         'annual_net_value_usd': modeled_net_benefit(
                             assumptions['baseline_review_hours_per_month'], rate, frac,
                             assumptions['annual_program_cost_usd'], assumptions['months'])})
    return pd.DataFrame(rows)


def set_style():
    plt.rcParams["svg.fonttype"] = "none"
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'axes.titlesize': 13,
                         'axes.labelcolor': INK, 'text.color': INK, 'axes.edgecolor': '#B8C7D3',
                         'axes.spines.top': False, 'axes.spines.right': False,
                         'savefig.facecolor': 'white', 'figure.facecolor': 'white'})


def save_figure(fig, output: Path, stem: str):
    fig.savefig(output / f'{stem}.png', dpi=175, bbox_inches='tight', facecolor='white')
    fig.savefig(output / f'{stem}.svg', bbox_inches='tight', facecolor='white')
    plt.close(fig)


def model_performance(metrics: dict, output: Path):
    """No ROC or PR curves are inferred from aggregate AUC values."""
    fig, axes = plt.subplots(1, 2, figsize=(11.7, 4.5), gridspec_kw={'width_ratios': [1.25, 1]})
    ax = axes[0]
    vals = [metrics['denial_prevalence'], metrics['denial_pr_auc']]
    bars = ax.barh(['No-skill prevalence', 'Model PR-AUC'], vals, color=['#B2C8D7', BLUE], height=0.52)
    ax.invert_yaxis(); ax.set_xlim(0, 0.36); ax.set_xlabel('Average precision / PR-AUC')
    ax.set_title('Finding rare denial cases'); ax.grid(axis='x', alpha=0.16)
    ax.set_axisbelow(True)
    for bar, v in zip(bars, vals):
        ax.text(v + 0.008, bar.get_y() + bar.get_height() / 2, f'{v:.3f}', va='center', weight='bold')
    ax.text(0.02, -0.34, f"{vals[1]/vals[0]:.1f}x baseline, retrospective patient-grouped validation",
            transform=ax.transAxes, fontsize=9, color=MUTED)
    ax2 = axes[1]
    ax2.axis('off')
    ax2.text(0.02, 0.80, '0.877', fontsize=33, weight='bold', color=NAVY, transform=ax2.transAxes)
    ax2.text(0.02, 0.69, 'ROC-AUC, denial-risk ranking', fontsize=11, transform=ax2.transAxes)
    ax2.text(0.02, 0.46, '0.967', fontsize=33, weight='bold', color=TEAL, transform=ax2.transAxes)
    ax2.text(0.02, 0.35, 'Mean F1, structured + clinical-text extraction', fontsize=10, transform=ax2.transAxes)
    ax2.text(0.02, 0.09, f"Retrospective evidence | {metrics['resolved_cases']:,} resolved cases for prediction",
             fontsize=9, color=MUTED, transform=ax2.transAxes)
    fig.suptitle('A  |  Predictive performance and research readiness', weight='bold', fontsize=15, x=0.02, ha='left')
    fig.subplots_adjust(top=0.79, bottom=0.22, wspace=0.34)
    save_figure(fig, output, '01_predictive_performance')


def workflow(metrics: dict, output: Path):
    fig, axs = plt.subplots(1, 2, figsize=(11.7, 4.7))
    ready = metrics['fully_ready_fraction'] * 100
    axs[0].barh(['Documentation status'], [100 - ready], color=PALE, height=0.52, label='Not fully ready')
    axs[0].barh(['Documentation status'], [ready], color=TEAL, height=0.52,
                left=[100 - ready], label='Fully ready')
    axs[0].set_xlim(0, 100); axs[0].set_xlabel('Share of assessed patients (%)')
    axs[0].set_title('Document completeness is uncommon')
    axs[0].text(1, 0, f'{ready:.1f}% fully ready', va='center', weight='bold', color=NAVY)
    axs[0].text(0.02, -0.27, 'Completeness definition follows the source research',
                transform=axs[0].transAxes, color=MUTED, fontsize=9)
    baseline = 100
    strict = baseline * (1 + metrics['strict_policy_tat_percent_longer'] / 100)
    bars = axs[1].barh(['Lenient policy', 'Strict policy'], [baseline, strict], color=['#B2C8D7', BLUE], height=0.50)
    axs[1].invert_yaxis(); axs[1].set_xlim(0, 220)
    axs[1].set_xlabel('Relative turnaround-time index (lenient = 100)')
    axs[1].set_title('Payer-policy groups differ in timing')
    for bar, v in zip(bars, [baseline, strict]):
        axs[1].text(v + 4, bar.get_y() + bar.get_height()/2, f'{v:.1f}', va='center', weight='bold')
    axs[1].text(0.02, -0.27, 'Indexed comparison, not absolute days or causal effect',
                transform=axs[1].transAxes, color=MUTED, fontsize=9)
    fig.suptitle('B  |  Operational signals for workflow prioritization', weight='bold', fontsize=15, x=0.02, ha='left')
    fig.subplots_adjust(top=0.79, bottom=0.24, wspace=0.39)
    save_figure(fig, output, '02_workflow_priorities')


def financial(table: pd.DataFrame, assumptions: dict, output: Path):
    frame = table.pivot(index='loaded_hourly_cost_usd', columns='avoidable_effort_pct',
                        values='annual_net_value_usd').sort_index(ascending=False)
    values = frame.to_numpy() / 1000
    extent = max(abs(values.min()), abs(values.max()), 1)
    cmap = LinearSegmentedColormap.from_list('balanced', ['#D5E2EC', '#F7FAFC', '#2B7795'])
    fig, ax = plt.subplots(figsize=(10.6, 5))
    im = ax.imshow(values, cmap=cmap, norm=TwoSlopeNorm(vmin=-extent, vcenter=0, vmax=extent), aspect='auto')
    ax.set_xticks(np.arange(len(frame.columns)), labels=[f'{c}%' for c in frame.columns])
    ax.set_yticks(np.arange(len(frame.index)), labels=[f'${r}/hour' for r in frame.index])
    ax.set_xlabel('Administrative effort avoided (scenario assumption)')
    ax.set_ylabel('Fully loaded labor rate (scenario assumption)')
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            v = values[i, j]
            ax.text(j, i, f'{"+" if v >= 0 else ""}${v:,.0f}k',
                    ha='center', va='center', fontsize=12, weight='bold', color=INK)
    fig.suptitle('C  |  Illustrative labor-only investment sensitivity', fontsize=15, weight='bold', x=0.02, ha='left')
    ax.set_title(f"Assumed {assumptions['baseline_review_hours_per_month']:,} h/month; "
                 f"${assumptions['annual_program_cost_usd']:,} annual program cost", color=MUTED, fontsize=10, pad=16)
    fig.text(0.07, 0.015, 'Hypothetical calculations only. No measured clinic savings, reimbursement effects, or causal estimates.',
             fontsize=9, color=MUTED)
    fig.subplots_adjust(top=0.76, bottom=0.22, left=0.16, right=0.95)
    save_figure(fig, output, '03_illustrative_financial_sensitivity')


def build(output: Path = HERE / 'figures') -> list[str]:
    output.mkdir(parents=True, exist_ok=True)
    data = load_evidence()
    metrics = data['retrospective_aggregates']
    assumptions = data['illustrative_financial_sensitivity']
    set_style()
    model_performance(metrics, output)
    workflow(metrics, output)
    table = sensitivity_table(assumptions)
    financial(table, assumptions, output)
    table.to_csv(output / 'illustrative_sensitivity_table.csv', index=False)
    (output / 'SOURCE_NOTES.md').write_text(
        '# Figure source notes\n\n'
        '- Figures 01 and 02 use previously reported, publicly summarized aggregate research results, '
        'specified in `../evidence_and_assumptions.json`; see `../../METRIC_PROVENANCE.md` and '
        '`../../results.md`. No individual predicted probabilities or patient rows are present.\n'
        '- Figure 02 uses a 100-point relative lenient-policy index and a 99.8% complement; '
        'these are arithmetic displays, not original raw observations.\n'
        '- Figure 03 is a transparent hypothetical scenario, not a Hidalga observed or modeled ROI estimate.\n'
        '- Regenerate: `python projects/05_clinical_ai_oncology/analytics/visualize.py`.\n',
        encoding='utf-8')
    return ['01_predictive_performance', '02_workflow_priorities', '03_illustrative_financial_sensitivity']


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=HERE / 'figures')
    args = parser.parse_args()
    stems = build(args.output)
    print('Generated', ', '.join(stems), 'at', args.output)
