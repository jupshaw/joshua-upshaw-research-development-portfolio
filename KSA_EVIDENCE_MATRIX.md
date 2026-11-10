# Knowledge, Skills, and Abilities Evidence Matrix

This matrix answers a hiring-manager question quickly: **what can Joshua do, where is the evidence, and why does it matter?**

| KSA | Evidence in this portfolio | R&D impact |
|---|---|---|
| Scientific problem formulation | Defined experimental and observational questions spanning distraction, attention, emotion, creativity, reward processing, behavioral health, and oncology workflow burden | Converts broad problems into measurable hypotheses and decision-ready endpoints |
| Experimental design | Navon oddball, mindfulness randomization, emotional dot-probe, auditory perturbations, behavioral and survey studies | Builds controlled tests that isolate mechanisms rather than only describing correlations |
| Neural signal analysis | EEG/ERP acquisition, N2/P2/P3, theta/alpha/beta, TBR, artifact control, ICA/ICLabel | Distinguishes physiological signal from recording and preprocessing artifacts |
| Multimodal measurement | Behavior + EEG; gaze + pupil + blink + saccade + RT; neuroimaging + behavioral variables; clinical text + structured EHR | Reduces dependence on a single noisy endpoint and supports convergent interpretation |
| Neuroimaging reasoning | ABCD ROI-based fMRI analysis plus earlier frontoparietal-network research on imagination | Connects network/ROI measures to cognitive hypotheses while calibrating claims to study design and effect magnitude |
| Behavioral and psychometric research | Alternate Uses Task, SemDis, CAQ, social-media measures, anxiety/loneliness measures, survey design, lab and field studies | Extends quantitative reasoning beyond physiological signals and supports construct-level interpretation |
| Statistical inference | Trial-level regression, repeated measures, mixed-effects models, moderation, effect-size interpretation | Matches inference to design and identifies when statistically significant effects remain practically small |
| Clinical data curation | Cohort construction, source reconciliation, missingness, duplicate events, label review, longitudinal case reconstruction | Turns operational EHR data into analysis-ready evidence while exposing measurement limitations |
| Applied machine learning | LightGBM rare-outcome prediction, ROC-AUC, PR-AUC, calibration, threshold/workload analysis | Converts model performance into operational decisions rather than optimizing metrics in isolation |
| Model-risk judgment | Leakage controls, patient grouping, temporal validation, calibration, distribution-shift thinking, human-review boundaries | Prevents retrospective performance from being misrepresented as deployment readiness |
| Data quality engineering | Source authority, malformed values, temporal anomalies, conflicting statuses, incomplete outcomes | Separates data and measurement problems from algorithm problems, improving corrective action |
| Reproducibility and provenance | RMarkdown, versioned pipelines, source lineage, dataset/model/result traceability | Makes findings auditable and supports scientific, regulatory, and technical due diligence |
| Human-subjects and clinical governance | IRB research, de-identification, HIPAA/HITECH, CITI GCP and human-subjects training, IRB Research Ethics Committee service | Enables responsible work with sensitive human and clinical data and strengthens research-governance judgment |
| Qualitative and mixed-methods analysis | Structured coding of interview data in behavioral-health research; stakeholder and workflow research in healthcare AI | Adds context to quantitative findings and improves requirements, interpretation, and implementation decisions |
| Scientific writing and peer review | First-author peer-reviewed papers, scholarly chapter, submitted clinical AI manuscript, ad hoc review for multiple journals | Demonstrates ability to construct, critique, and communicate evidence to scientific audiences |
| Teaching and nonexpert communication | Instructor of record for four university General Psychology sections; technical presentations across scientific and executive audiences | Demonstrates ability to translate complex concepts without losing scientific accuracy |
| Technical claims governance | Explicit separation of observed, retrospective, simulated, modeled, prospective, and causal claims | Reduces scientific, regulatory, commercial, and reputational risk |
| Cross-functional translation | NSF PI leadership across clinical, engineering, operations, compliance, executive, and external stakeholders | Converts technical evidence into requirements, risks, next actions, and investment decisions |
| Research-to-product judgment | Retrospective feasibility -> telemetry specification -> staged prospective pilot | Uses research to define what should be built and what evidence is required before scaling |

## Public analytics and visualization artifacts (new portfolio enhancement)

| Capability | Inspectable artifact | What the artifact demonstrates | Evidence status |
|---|---|---|---|
| Data visualization | [Figures A-C](projects/05_clinical_ai_oncology/analytics/README.md) | Designed audience-specific performance, workflow and sensitivity comparisons | Retrospective aggregates for A/B; illustrative assumptions for C |
| Python analytical programming | [visualize.py](projects/05_clinical_ai_oncology/analytics/visualize.py) | Loads validated inputs, transforms summary metrics, renders vector and raster assets | New portfolio code, not original Phase I source |
| Quantitative interpretation | [Analytical report](projects/05_clinical_ai_oncology/analytics/REPORT.md) | Interprets rare-event PR-AUC against prevalence and flags causal/operational limits | Retrospective single-site finding |
| Business intelligence | [Workflow figure](projects/05_clinical_ai_oncology/analytics/figures/02_workflow_priorities.svg) | Reports completeness and indexed payer timing as signals for measurement priorities | Aggregate/derived, not causally estimated |
| Strategic decision support | [Illustrative sensitivity model](projects/05_clinical_ai_oncology/analytics/evidence_and_assumptions.json) | Links assumed workload, labor rate, effort avoided and program cost to conditional net value | Hypothetical example, no actual clinic ROI |
| Data quality and provenance | [Source notes](projects/05_clinical_ai_oncology/analytics/figures/SOURCE_NOTES.md) and [tests](tests/test_analytics_visualization.py) | Checks fraction bounds, source contexts, scenario arithmetic and output completeness | Verified local portfolio artifacts |
| Executive communication | [Report](projects/05_clinical_ai_oncology/analytics/REPORT.md) | Business question, method, visual, interpretation, recommendation and limitation per analysis | Newly authored portfolio material |

**Attribution:** These files demonstrate a new portfolio enhancement created with AI-assisted development. They must not be recast as code independently written during the original NSF SBIR Phase I study.
