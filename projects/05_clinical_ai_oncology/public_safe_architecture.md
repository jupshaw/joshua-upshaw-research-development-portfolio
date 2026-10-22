# Public-Safe Architecture View

This page intentionally omits partner-specific interfaces, production credentials, proprietary payer criteria, and trade-secret implementation details.

```mermaid
flowchart TD
    A[EHR / operational sources] --> B[Normalization + provenance]
    B --> C[Clinical evidence layer]
    B --> D[Workflow state layer]
    C --> E[Extraction / rules / ML services]
    D --> E
    E --> F[Human review + recommendation interface]
    F --> G[Telemetry + outcomes]
    G --> H[Validation / monitoring]
```

## Design patterns demonstrated

- Source-grounded evidence
- Provenance and field-level traceability
- Hybrid structured data + targeted NLP
- Separate validation strategies for extraction, deterministic rules, and prediction
- Human-in-the-loop authority boundaries
- Versioned schemas / contracts
- Prospective telemetry
- Security and privacy as architecture constraints
