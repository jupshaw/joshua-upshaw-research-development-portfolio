# Results, Limitations, and Decision Impact

## Clinical information extraction

Combined structured + free-text extraction reached **F1 = 0.967** across the confirmatory field set. Standalone free-text NLP was materially weaker, reinforcing a **structured-first, NLP-where-needed** design philosophy.

Only about **0.2%** of cases met the defined complete PA-readiness criteria. This transformed "documentation burden" from a general complaint into a measurable intervention target.

## Rare-outcome prediction

On 96,261 resolved cases:

- ROC-AUC = **0.877**
- PR-AUC = **0.289**
- No-skill PR baseline = **0.024**
- Brier score after sigmoid calibration = **0.052**
- Expected calibration error = **0.064**

The model was defined as **review triage**, not an autonomous approve/deny predictor.

## Workflow timing

Reported comparisons showed substantially longer TAT in stricter payer-policy groups. Rework signals such as request-for-information events were associated with longer workflow durations.

## Simulation vs observation

A calibrated workflow simulation projected **15%+ shorter median TAT** and improved approval rate under modeled routing. These results are labeled **simulated** and are not represented as real-world intervention effects.

## Core limitation

Historical records captured outcomes more reliably than the staff actions that produced them. The retrospective data therefore could not establish the causal effect of a recommended staff action on payer turnaround time.

## R&D impact

Instead of hiding that limitation, the program converted it into a prospective instrumentation requirement: action eligibility, action selected, recommendation exposure, override/reason, timestamp, payer response, workload, and final outcome.
