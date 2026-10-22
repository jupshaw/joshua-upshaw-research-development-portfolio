<div align="center">

![Research & Development Portfolio](assets/profile_banner.svg)

# Joshua Daniel Upshaw, PhD

**Clinical Data Science · Cognitive Neuroscience · Applied Machine Learning · Real-World Evidence**

*A research and development portfolio spanning human neuroscience, multimodal experimental methods, clinical data science, and healthcare AI.*

[![Google Scholar](https://img.shields.io/badge/Google_Scholar-Publications-4285F4?style=for-the-badge)](https://scholar.google.com/citations?user=XAe-ESMAAAAJ&hl=en)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-0A66C2?style=for-the-badge)](https://www.linkedin.com/in/joshua-upshaw-ph-d/)
[![Email](https://img.shields.io/badge/Email-Contact-555555?style=for-the-badge)](mailto:jupshaw2010@gmail.com)

`EEG / ERP` · `Spectral EEG` · `1000 Hz eye tracking` · `fMRI` · `Longitudinal EHR` · `Clinical NLP` · `Rare-outcome ML`

</div>

---

I build research systems that turn complex human and clinical data into defensible evidence. My work spans controlled cognitive neuroscience experiments, EEG/ERP and spectral signal analysis, 1000 Hz eye tracking, secondary fMRI analysis, behavioral science, longitudinal EHR data, clinical NLP, rare-outcome machine learning, and prospective study design.

> [!IMPORTANT]
> **The unifying theme is measurement discipline:** define the phenomenon carefully, protect signal and data quality, match the analysis to the decision, calibrate claims to the evidence, and design the next experiment around what remains uncertain.

### Where to start

| If you are… | Start here |
|---|---|
| **An executive** | [START_HERE.md](START_HERE.md) and the [flagship projects](#flagship-projects) table |
| **A scientist or engineer** | The [project folders](projects/), [METHODS_MATRIX.md](METHODS_MATRIX.md), and synthetic demos in [`examples/`](examples/) |
| **A hiring team** | [KSA_EVIDENCE_MATRIX.md](KSA_EVIDENCE_MATRIX.md), a concise map from capability to evidence and impact |

---

## Executive readout

My work has moved through three increasingly complex research environments:

| | Environment | What it involved |
|:-:|---|---|
| **1** | **Controlled human psychophysiological experiments** | Manipulating attention, auditory distraction, mindfulness behavioral intervention, and emotional stimuli while measuring behavior, EEG, ERPs, spectral activity, gaze, pupil dynamics, saccades, and individual psychological traits |
| **2** | **Large observational neuroscience datasets** | Testing moderation hypotheses in ABCD fMRI data while explicitly distinguishing statistical significance from explanatory magnitude |
| **3** | **Real-world clinical AI** | Reconstructing longitudinal oncology workflows from heterogeneous EHR data, evaluating NLP and rare-outcome ML, identifying data-quality constraints, and converting retrospective limitations into prospective measurement requirements |

This progression supports a broader R&D capability:

<div align="center">

**question → measurement system → data pipeline → model → validation → bounded claim → next experiment → implementation decision**

</div>

```mermaid
flowchart LR
    subgraph EXP["Controlled experiments"]
        direction LR
        A[Behavioral science] --> B[EEG / ERP] --> C[Spectral EEG] --> D[1000 Hz eye tracking]
    end
    subgraph OBS["Observational neuroscience"]
        E[fMRI secondary analysis]
    end
    subgraph CLIN["Real-world clinical AI"]
        direction LR
        F[Clinical RWE + NLP + ML] --> G[Prospective pilot design]
    end
    D --> E --> F

    classDef exp fill:#E8F0FE,stroke:#4285F4,color:#1A1A1A;
    classDef obs fill:#F3E8FD,stroke:#8E44AD,color:#1A1A1A;
    classDef clin fill:#E6F4EA,stroke:#2E7D32,color:#1A1A1A;
    class A,B,C,D exp;
    class E obs;
    class F,G clin;
```

---

## Flagship projects

| Project | Problem | Methods | Selected result | Evidence status |
|---|---|---|---|---|
| 🧠 **[EEG/ERP: digital distraction](projects/01_eeg_erp_digital_distraction/)** | Does an ecologically familiar auditory cue alter cognitive-control processing? | BioSemi EEG, ERP, Navon oddball, trial-level regression, ICA/ICLabel | Smartphone-sound trials were slightly slower; N2 differed by sound condition while P3 did not | ![](https://img.shields.io/badge/Peer_reviewed-First_author-2E7D32) |
| 📈 **[Spectral EEG + mindfulness](projects/02_spectral_eeg_mindfulness/)** | How do notifications and a brief mindfulness induction alter task-locked spectral dynamics? | 32-channel EEG, ASR, Infomax ICA, ICLabel, theta/alpha/beta, TBR | Notifications altered spectral power; selected group contrasts emerged, but the omnibus group × sound TBR interaction was not significant | ![](https://img.shields.io/badge/Peer_reviewed-First%2Fcorresponding_author-2E7D32) |
| 👁️ **[Eye tracking + emotional attention](projects/03_eye_tracking_emotional_attention/)** | How do auditory notifications interact with emotional visual attention? | EyeLink 1000 Plus, PsychoPy, 1000 Hz gaze, pupil, fixation, saccade, blink, mixed models | Angry faces delayed first fixation vs. happy faces; notification trials increased pupil variability vs. silence | ![](https://img.shields.io/badge/PhD_dissertation-OSF_preregistered-1565C0) |
| 🧲 **[fMRI + reward processing](projects/04_fmri_reward_processing/)** | Is youth screen time associated with reward/risk circuitry, and is that relationship moderated by caregiver warmth? | ABCD, MID task, ROI BOLD, R/RMarkdown, regression/moderation | Significant right anterior-insula interaction, but adjusted R² was only 0.0073 | ![](https://img.shields.io/badge/Graduate_course_project-Not_peer_reviewed-757575) |
| 🏥 **[Clinical AI + oncology RWE](projects/05_clinical_ai_oncology/)** | Can heterogeneous oncology records support evidence extraction, denial-risk triage, workflow analysis, and prospective intervention design? | Longitudinal EHR, clinical NLP, LightGBM, grouped validation, PR-AUC, calibration, timing analysis, simulation | Combined extraction F1 0.967; denial ROC-AUC 0.877 and PR-AUC 0.289; retrospective limitations drove prospective telemetry design | ![](https://img.shields.io/badge/NSF_SBIR_Phase_I-Retrospective_feasibility-E65100) |

---

## Methods and tools

| Domain | Methods | Tools / technologies |
|---|---|---|
| **Neural signals** | EEG acquisition, ERP analysis, task-locked spectral power, artifact detection, ICA, source-component classification | `BioSemi ActiveTwo` `Net Station` `EEGLAB` `ERPLAB` `MATLAB` `ICLabel` |
| **Eye tracking** | Calibration/validation, AOI analysis, first fixation, saccades, blinks, pupil magnitude/variability, trial QC | `EyeLink 1000 Plus` `PsychoPy` `Data Viewer` `R` |
| **Neuroimaging** | ROI-based BOLD analysis, moderation, transformed predictors, motion/outlier exclusion | `ABCD data` `MID task` `R` `RStudio` `RMarkdown` |
| **Clinical data science** | Cohort construction, longitudinal case reconstruction, source reconciliation, data-quality engineering, clinical NLP | `Python` `pandas` `SQL` `PostgreSQL` `Jupyter` |
| **Machine learning** | Rare-outcome modeling, grouped/temporal validation, ROC-AUC, PR-AUC, calibration, threshold/workload analysis | `scikit-learn` `LightGBM` `XGBoost` `Optuna` |
| **Healthcare systems** | Clinical terminology normalization, provenance, interoperability, data contracts | `FHIR R4` `HL7` `X12` `REST APIs` `Azure` |
| **Research governance** | IRB/human subjects, de-identification, HIPAA, GCP, claims calibration, reproducibility | `CITI GCP / Human Subjects / HIPAA` `Git` `Versioned analyses` |

📎 **Go deeper:** [METHODS_MATRIX.md](METHODS_MATRIX.md) (project-level evidence) · [TECHNICAL_TOOLKIT.md](TECHNICAL_TOOLKIT.md) (capability inventory) · [RESEARCH_AND_DEVELOPMENT_APPROACH.md](RESEARCH_AND_DEVELOPMENT_APPROACH.md) (end-to-end research-to-product process)

---

## How I evaluate evidence

I intentionally keep these distinctions separate:

| This… | …is not the same as this |
|---|---|
| Observed results | Simulated results |
| Association | Prediction |
| Prediction | Intervention effects |
| Retrospective performance | Prospective performance |
| Statistical significance | Practical or explanatory magnitude |
| Model limitations | Measurement and source-data limitations |

This is not just a reporting preference. It determines what can safely be built, tested, communicated, or deployed.

---

## Core knowledge, skills, and abilities

<table>
<tr>
<td valign="top" width="50%">

**Research & measurement**
- Experimental design and hypothesis decomposition
- Multimodal human-data acquisition and synchronization
- Neural-signal and physiological-data quality control
- Longitudinal clinical-data curation and source reconciliation
- Statistical modeling and rare-outcome machine learning

</td>
<td valign="top" width="50%">

**Rigor, governance & leadership**
- Leakage control, calibration, temporal validation, and model-risk evaluation
- Reproducibility, provenance, requirements traceability, and technical claims governance
- Human-subjects research, privacy, and clinical-data governance
- Cross-functional translation across science, engineering, clinical operations, product, and executives
- Research-program leadership and research-to-commercialization judgment

</td>
</tr>
</table>

Evidence for each is mapped in [KSA_EVIDENCE_MATRIX.md](KSA_EVIDENCE_MATRIX.md).

---

## Additional projects

The repository also includes work on divergent thinking and social-media behavior, imagination and anxiety during COVID-19, attention/affect/creativity synthesis, mindfulness and health behavior, developmental psychophysiology, social psychology, and anxiety/substance-use research. See [`projects/06_additional_projects/`](projects/06_additional_projects/).

---

## Public-safe reproducibility examples

The [`examples/`](examples/) folder contains synthetic demonstrations of EEG quality control, eye-tracking analysis, and rare-outcome clinical ML validation.

> [!NOTE]
> These are **not** the original participant-level or clinical datasets and are **not** representations of proprietary production code. They exist to make the analytical reasoning inspectable without exposing protected, licensed, confidential, or proprietary material.

---

## Repository map

<details>
<summary><b>Expand folder structure</b></summary>

```text
projects/      Flagship and additional research case studies
methods/       Reusable method notes and decision frameworks
examples/      Synthetic, executable demonstrations
notebooks/     Jupyter notebooks for public-safe demonstrations
docs/          Executive summary, publications, certifications, portfolio PDF
assets/        Recreated/public-safe figures and diagrams
.github/       Lightweight validation workflow
```

</details>

## Research portfolio PDF

📄 A polished narrative version of this work is included at [`docs/Joshua_Upshaw_Research_Portfolio.pdf`](docs/Joshua_Upshaw_Research_Portfolio.pdf).

---

## Data, IP, and privacy

> [!WARNING]
> No PHI, clinic-level raw exports, participant-level restricted data, payer proprietary criteria, production credentials, or confidential source reports are included. See [PUBLIC_DATA_AND_IP_POLICY.md](PUBLIC_DATA_AND_IP_POLICY.md).