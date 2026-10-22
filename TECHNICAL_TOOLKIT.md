# Technical Toolkit

This inventory is organized by **how the tools were used**, not as a keyword list. Depth varies by project; training-only or secondary exposure is labeled accordingly.

| Domain | Tools / methods | Portfolio evidence | Typical use |
|---|---|---|---|
| EEG acquisition | BioSemi ActiveTwo, Net Station | Smartphone notification studies; developmental psychophysiology lab | Human electrophysiology acquisition, event synchronization, recording QA |
| EEG analysis | MATLAB, EEGLAB, ERPLAB, ASR, Infomax ICA, ICLabel | ERP and spectral EEG projects | Artifact handling, source-component review, ERP windows, theta/alpha/beta/TBR analysis |
| Additional EEG software | Brainstorm, EMSE Suite | Professional training and prior technical work | Secondary EEG/ERP processing environments; not presented here as primary platforms for flagship analyses |
| Experimental task systems | PsychoPy, E-Prime, Presentation | Eye-tracking and EEG paradigms | Stimulus timing, behavioral response collection, event synchronization |
| Eye tracking | EyeLink 1000 Plus, Data Viewer | PhD dissertation | 1000 Hz gaze acquisition, calibration, AOI/fixation, saccade, blink, pupil analysis |
| Behavioral and survey research | Qualtrics, SPSS, SemDis, structured interview coding | Creativity, social cognition, anxiety/substance-use, and affective research | Survey deployment, psychometrics, semantic scoring, behavioral statistics, qualitative coding |
| Neuroimaging | R, RStudio, RMarkdown, ROI-based BOLD analysis, moderation | ABCD fMRI project; earlier frontoparietal-network research | Secondary neuroimaging analysis, reproducible modeling, effect-size and limitation interpretation |
| Statistical computing | R, RStudio, RMarkdown, MATLAB, SPSS | fMRI, eye tracking, behavioral research, EEG | Regression, moderation, repeated measures, mixed-effects workflows, reproducible reporting |
| Python data science | Python, NumPy, pandas, scikit-learn, Jupyter | NSF SBIR clinical data science | Data curation, feature engineering, ML evaluation, reproducible analysis |
| Gradient boosting / optimization | LightGBM, XGBoost, Optuna | Healthcare AI research | Rare-outcome prediction, model comparison, hyperparameter search |
| Clinical data engineering | SQL, PostgreSQL, CSV/JSON/Parquet, ETL/ELT | Oncology EHR research | Joining, normalization, longitudinal episode reconstruction, source reconciliation |
| Clinical NLP / informatics | Clinical NLP/NER, ICD-10, CPT/HCPCS, LOINC, SNOMED CT, RxNorm, NDC | Oncology evidence extraction | Terminology normalization, biomarker/stage/regimen extraction, evidence provenance |
| Healthcare interoperability | FHIR R4, HL7, X12, REST/OpenAPI | Hidalga systems architecture | Data/interface contracts and EHR/payer integration design |
| Cloud / platform | Microsoft Azure, Azure Health Data Services, Azure ML, Supabase | Hidalga R&D platform | Secure healthcare data and ML infrastructure |
| Versioning / reproducibility | Git, GitHub, versioned datasets/schemas, provenance | Academic and industry research | Traceable transformations, model artifacts, collaborative development |
| Research governance | IRB, informed consent, de-identification, HIPAA/HITECH, ICH-GCP | Human neuroscience + clinical AI | Human-subjects protection, privacy, regulated research operations |
| Scientific communication | Peer review, manuscript development, conference talks/posters, university teaching | Publications, reviewer service, Instructor of Record, research presentations | Technical critique, scientific storytelling, nonexpert explanation, stakeholder alignment |

## Selected professional training

- CITI Good Clinical Practice, ICH-focused investigator-site training
- CITI Biomedical Human Subjects Research
- CITI Health Privacy / HIPAA and information security
- CITI Responsible Conduct of Research
- EEG/ERP Boot Camp: From Data to Treatment, Andreas Muller, PhD, 2022
- Arkansas Children's Hospital Brainstorm Software Training, 2024
- NSF I-Corps and research commercialization training

## Technical decision skills

Tools are most useful when paired with judgment. Across projects, the recurring technical decisions were:

- whether a variable was measured well enough to model;
- whether an artifact or source-data problem could explain a result;
- whether a feature existed at the real decision time;
- whether class imbalance made a headline metric misleading;
- whether a statistically significant result had meaningful magnitude;
- whether a retrospective result supported research, silent evaluation, recommendation, or deployment;
- what instrumentation the next study needed to collect;
- how to communicate uncertainty differently to scientists, engineers, clinicians, and executives.
