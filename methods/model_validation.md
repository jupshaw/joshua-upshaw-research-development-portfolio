# Machine-Learning Validation and Model Risk

## Rare-outcome evaluation

For low-prevalence outcomes, accuracy and ROC-AUC alone can be misleading. Evaluation should include:

- prevalence / no-skill baseline
- ROC-AUC
- precision-recall AUC
- recall and precision at candidate thresholds
- calibration
- false-positive workload
- feature availability at decision time
- grouped validation
- temporal validation
- subgroup stability
- drift and monitoring requirements

## Deployment ladder

```mermaid
flowchart LR
    A[Research] --> B[Offline validation]
    B --> C[Simulation]
    C --> D[Silent observation]
    D --> E[Staff-facing recommendation]
    E --> F[Workflow assistance]
    F --> G[Higher automation only with new evidence]
```

A model should advance only when the evidence supports the next level of authority.
