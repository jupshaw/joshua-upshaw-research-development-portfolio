# Project Index

Fast comparison of the portfolio's flagship work. Evidence labels are intentionally explicit so peer-reviewed, dissertation, course-project, retrospective, and synthetic evidence are not treated as equivalent.

| Project | Evidence | Data / scale | Core methods | Main contribution | Primary limitation |
|---|---|---|---|---|---|
| [EEG/ERP: digital distraction](projects/01_eeg_erp_digital_distraction/) | Peer reviewed, first author | 73 recruited; 69 behavioral; 54 ERP; 960 trials/person | BioSemi EEG, ICA/ICLabel, ERP, trial-level regression | Selective neural/behavioral effects with bounded interpretation | Smaller ERP sample after QC; several null moderation effects |
| [Spectral EEG + mindfulness](projects/02_spectral_eeg_mindfulness/) | Peer reviewed, first/corresponding author | 101 eligible; 87 final EEG | ASR, Infomax ICA, ICLabel, theta/alpha/beta, TBR | Frequency-domain extension with transparent correction and mixed/null findings | Primary group x sound TBR interaction not significant |
| [Eye tracking: emotional attention](projects/03_eye_tracking_emotional_attention/) | PhD dissertation, OSF preregistered | 50 participants; 360 trials/person; 1000 Hz | Fixation/AOI, saccade, blink, pupil, repeated measures | High-resolution decomposition of visual orienting and physiological response | Endpoint-specific usable samples and multiple null outcomes |
| [fMRI: reward processing](projects/04_fmri_reward_processing/) | Graduate course project | 1,119 ABCD participants | ROI BOLD, regression, moderation, R/RMarkdown | Effect-size discipline and secondary neuroimaging analysis | Observational design; very small explained variance |
| [Clinical AI: oncology RWE](projects/05_clinical_ai_oncology/) | NSF SBIR Phase I retrospective feasibility | 24,167 patients; 200,513 PA records; 148,703 notes | NLP, cohort reconstruction, LightGBM, grouped/temporal validation, calibration | Clinical extraction, risk triage, workflow analysis, prospective instrumentation | Historical actions insufficient for causal workflow claims |
| [Additional projects](projects/06_additional_projects/) | Mixed evidence tiers | Behavioral, psychometric, psychophysiology, intervention, social cognition | Quantitative + qualitative methods | Cross-domain breadth and adaptation | Evidence depth varies by project |

## Technical review shortcuts

- **Neuroscience methods:** [projects/01](projects/01_eeg_erp_digital_distraction/) -> [projects/02](projects/02_spectral_eeg_mindfulness/) -> [projects/03](projects/03_eye_tracking_emotional_attention/) -> [projects/04](projects/04_fmri_reward_processing/)
- **Clinical data science / ML:** [Clinical AI project](projects/05_clinical_ai_oncology/) -> [Model Card](projects/05_clinical_ai_oncology/MODEL_CARD.md) -> [Metric Provenance](projects/05_clinical_ai_oncology/METRIC_PROVENANCE.md)
- **Executable examples:** [examples/](examples/) and [notebooks/](notebooks/)
- **Methods crosswalk:** [METHODS_MATRIX.md](METHODS_MATRIX.md)
