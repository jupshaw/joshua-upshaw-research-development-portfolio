# Technical Notes

The study demonstrates a full neural-analysis chain:

```mermaid
flowchart LR
    A[Controlled task] --> B[EEG + EOG acquisition]
    B --> C[Filtering / channel QC]
    C --> D[ASR + ICA]
    D --> E[ICLabel]
    E --> F[Epoching]
    F --> G[Theta / Alpha / Beta]
    F --> H[ERP windows]
    G --> I[Repeated-measures inference]
    H --> I
    I --> J[Positive + null result interpretation]
```

The portfolio does not redistribute publisher figures. The repository instead summarizes reported results and links to the DOI.
