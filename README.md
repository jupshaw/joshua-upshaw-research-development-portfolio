![Research & Development Portfolio](assets/profile_banner.svg)

# Joshua Daniel Upshaw, PhD
## Research & Development Portfolio

**Clinical Data Science | Cognitive Neuroscience | Applied Machine Learning | Real-World Evidence**

[Google Scholar](https://scholar.google.com/citations?user=XAe-ESMAAAAJ&hl=en) | [LinkedIn](https://www.linkedin.com/in/joshua-upshaw-ph-d/) | [Email](mailto:jupshaw2010@gmail.com)

I build research systems that turn complex human and clinical data into defensible evidence. My work spans controlled cognitive neuroscience experiments, EEG/ERP and spectral signal analysis, 1000 Hz eye tracking, secondary fMRI analysis, behavioral science, longitudinal EHR data, clinical NLP, rare-outcome machine learning, and prospective study design.

The unifying theme is **measurement discipline**: define the phenomenon carefully, protect signal and data quality, match the analysis to the decision, calibrate claims to the evidence, and design the next experiment around what remains uncertain.

> **For executives:** start with [START_HERE.md](START_HERE.md) and the flagship-project table below.  
> **For scientists and engineers:** open the project folders, [METHODS_MATRIX.md](METHODS_MATRIX.md), and the synthetic demonstrations in [`examples/`](examples/).  
> **For hiring teams:** see [KSA_EVIDENCE_MATRIX.md](KSA_EVIDENCE_MATRIX.md) for a concise map from capability to evidence and impact.

---

## Executive readout

I have worked across three increasingly complex research environments:

1. **Controlled human experiments** - manipulating attention, auditory distraction, mindfulness, and emotional stimuli while measuring behavior, EEG, ERPs, spectral activity, gaze, pupil dynamics, and saccades.
2. **Large observational neuroscience datasets** - testing moderation hypotheses in ABCD fMRI data while explicitly distinguishing statistical significance from explanatory magnitude.
3. **Real-world clinical AI** - reconstructing longitudinal oncology workflows from heterogeneous EHR data, evaluating NLP and rare-outcome ML, identifying data-quality constraints, and converting retrospective limitations into prospective measurement requirements.

This progression supports a broader R&D capability: **question -> measurement system -> data pipeline -> model -> validation -> bounded claim -> next experiment -> implementation decision**.

```mermaid
flowchart LR
    A[Behavioral science] --> B[EEG / ERP]
    B --> C[Spectral EEG]
    C --> D[1000 Hz eye tracking]
    D --> E[fMRI secondary analysis]
    E --> F[Clinical RWE + NLP + ML]
    F --> G[Prospective pilot design]
```

## Flagship projects

| Project | Problem | Methods | Selected result | Evidence status |
|---|---|---|---|---|
| [EEG/ERP: digital distraction](projects/01_eeg_erp_digital_distraction/) | Does an ecologically familiar auditory cue alter cognitive-control processing? | BioSemi EEG, ERP, Navon oddball, trial-level regression, ICA/ICLabel | Smartphone-sound trials were slightly slower; N2 differed by sound condition while P3 did not | **Peer reviewed, first author** |
| [Spectral EEG + mindfulness](projects/02_spectral_eeg_mindfulness/) | How do notifications and a brief mindfulness induction alter task-locked spectral dynamics? | 32-channel EEG, ASR, Infomax ICA, ICLabel, theta/alpha/beta, TBR | Notifications altered spectral power; selected group contrasts emerged, but the omnibus group x sound TBR interaction was not significant | **Peer reviewed, first/corresponding author** |
| [Eye tracking + emotional attention](projects/03_eye_tracking_emotional_attention/) | How do auditory notifications interact with emotional visual attention? | EyeLink 1000 Plus, PsychoPy, 1000 Hz gaze, pupil, fixation, saccade, blink, mixed models | Angry faces delayed first fixation vs happy faces; notification trials increased pupil variability vs silence | **PhD dissertation, OSF preregistered** |
| [fMRI + reward processing](projects/04_fmri_reward_processing/) | Is youth screen time associated with reward/risk circuitry, and is that relationship moderated by caregiver warmth? | ABCD, MID task, ROI BOLD, R/RMarkdown, regression/moderation | Significant right anterior-insula interaction, but adjusted R2 was only 0.0073 | **Graduate course project, not peer reviewed** |
| [Clinical AI + oncology RWE](projects/05_clinical_ai_oncology/) | Can heterogeneous oncology records support evidence extraction, denial-risk triage, workflow analysis, and prospective intervention design? | Longitudinal EHR, clinical NLP, LightGBM, grouped validation, PR-AUC, calibration, timing analysis, simulation | Combined extraction F1 0.967; denial ROC-AUC 0.877 and PR-AUC 0.289; retrospective limitations drove prospective telemetry design | **NSF SBIR Phase I, retrospective feasibility research** |

## Methods and tools

| Domain | Methods | Tools / technologies |
|---|---|---|
| Neural signals | EEG acquisition, ERP analysis, task-locked spectral power, artifact detection, ICA, source-component classification | BioSemi ActiveTwo, Net Station, EEGLAB, ERPLAB, MATLAB, ICLabel |
| Eye tracking | Calibration/validation, AOI analysis, first fixation, saccades, blinks, pupil magnitude/variability, trial QC | EyeLink 1000 Plus, PsychoPy, Data Viewer, R |
| Neuroimaging | ROI-based BOLD analysis, moderation, transformed predictors, motion/outlier exclusion | ABCD data, MID task, R, RStudio, RMarkdown |
| Clinical data science | Cohort construction, longitudinal case reconstruction, source reconciliation, data-quality engineering, clinical NLP | Python, pandas, SQL, PostgreSQL, Jupyter |
| Machine learning | Rare-outcome modeling, grouped/temporal validation, ROC-AUC, PR-AUC, calibration, threshold/workload analysis | scikit-learn, LightGBM, XGBoost, Optuna |
| Healthcare systems | Clinical terminology normalization, provenance, interoperability, data contracts | FHIR R4, HL7, X12, REST APIs, Azure |
| Research governance | IRB/human subjects, de-identification, HIPAA, GCP, claims calibration, reproducibility | CITI GCP/Human Subjects/HIPAA training, Git, versioned analyses |

See [METHODS_MATRIX.md](METHODS_MATRIX.md) for project-level evidence.

For a deeper capability inventory, see [TECHNICAL_TOOLKIT.md](TECHNICAL_TOOLKIT.md). For the end-to-end research-to-product process, see [RND_OPERATING_MODEL.md](RND_OPERATING_MODEL.md).

## How I evaluate evidence

I intentionally separate:

- **observed** results from simulated results;
- **association** from prediction;
- **prediction** from intervention effects;
- **retrospective performance** from prospective performance;
- **statistical significance** from practical or explanatory magnitude;
- **model limitations** from measurement and source-data limitations.

This is not just a reporting preference. It determines what can safely be built, tested, communicated, or deployed.

## Core knowledge, skills, and abilities

- Experimental design and hypothesis decomposition
- Multimodal human-data acquisition and synchronization
- Neural-signal and physiological-data quality control
- Longitudinal clinical-data curation and source reconciliation
- Statistical modeling and rare-outcome machine learning
- Leakage control, calibration, temporal validation, and model-risk evaluation
- Reproducibility, provenance, requirements traceability, and technical claims governance
- Human-subjects research, privacy, and clinical-data governance
- Cross-functional translation across science, engineering, clinical operations, product, and executives
- Research-program leadership and research-to-commercialization judgment

Evidence for each is mapped in [KSA_EVIDENCE_MATRIX.md](KSA_EVIDENCE_MATRIX.md).

## Additional projects

The repository also includes work on divergent thinking and social-media behavior, imagination and anxiety during COVID-19, attention/affect/creativity synthesis, mindfulness and health behavior, developmental psychophysiology, social psychology, and anxiety/substance-use research. See [`projects/06_additional_projects/`](projects/06_additional_projects/).

## Public-safe reproducibility examples

The [`examples/`](examples/) folder contains synthetic demonstrations of EEG quality control, eye-tracking analysis, and rare-outcome clinical ML validation. These are **not** the original participant-level or clinical datasets and are **not** representations of proprietary production code. They exist to make the analytical reasoning inspectable without exposing protected, licensed, confidential, or proprietary material.

## Repository map

```text
projects/      Flagship and additional research case studies
methods/       Reusable method notes and decision frameworks
examples/      Synthetic, executable demonstrations
notebooks/     Jupyter notebooks for public-safe demonstrations
docs/          Executive summary, publications, certifications, portfolio PDF
assets/        Recreated/public-safe figures and diagrams
.github/       Lightweight validation workflow
```

## Research portfolio PDF

A polished narrative version of this work is included at [`docs/Joshua_Upshaw_Research_Portfolio.pdf`](docs/Joshua_Upshaw_Research_Portfolio.pdf).

## Data, IP, and privacy

No PHI, clinic-level raw exports, participant-level restricted data, payer proprietary criteria, production credentials, or confidential source reports are included. See [PUBLIC_DATA_AND_IP_POLICY.md](PUBLIC_DATA_AND_IP_POLICY.md).
