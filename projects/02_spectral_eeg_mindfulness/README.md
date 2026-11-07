# Spectral EEG: Notifications, Mindfulness, and Cognitive Control

**Evidence status:** Peer-reviewed, first and corresponding author  
**Publication:** *Biological Psychology* (2023), 185, 108725  
**DOI:** https://doi.org/10.1016/j.biopsycho.2023.108725

## Executive readout

**Problem:** ERP peaks capture time-locked responses but do not fully characterize oscillatory neural dynamics during distraction.  
**Approach:** Extend the notification paradigm to theta, alpha, beta, and theta/beta-ratio measures after randomized mindfulness vs neutral narration.  
**Result:** Notifications altered task-locked spectral power and selected mindfulness-related contrasts emerged, but the omnibus group x sound TBR interaction was not significant. Interpretation was deliberately bounded.

## My role

- First and corresponding author
- Study design and experimental execution
- EEG preprocessing and spectral analysis
- Statistical interpretation and manuscript development
- Correction and transparent reporting of a peer-review-identified preprocessing statistic error

## Data / study scale

| Measure | Value |
|---|---:|
| Eligible participants | 101 |
| EEG datasets before preprocessing | 97 |
| Final EEG sample | 87 |
| Mindfulness / control | 44 / 43 |
| EEG channels | 32 active electrodes |
| Acquisition rate | 512 Hz |

## Methods and technical implementation

BioSemi ActiveTwo, MATLAB, EEGLAB, artifact subspace reconstruction, extended Infomax ICA, ICLabel, event-locked epochs, theta/alpha/beta spectral analyses, theta/beta ratio, and repeated-measures inference.

See [methods.md](methods.md) and [technical_notes.md](technical_notes.md).

## Results

Notifications altered selected spectral bands. Some follow-up contrasts suggested condition-specific differences, but the broad group x sound TBR interaction was not statistically significant.

See [results.md](results.md).

## What changed because of the result

The nonsignificant primary interaction prevented a generalized claim that brief mindfulness improved cognitive control under smartphone distraction. The mixed pattern reinforced a research principle used throughout this portfolio: **follow-up contrasts do not override the evidentiary meaning of the primary interaction.**

## Limitations

- Primary group x sound TBR interaction not significant
- Some effects were condition-specific rather than general
- Short mindfulness induction does not establish durable intervention effects
- Participant-level EEG remains restricted

## Reproducibility / public artifacts

A synthetic event-based EEG workflow is available in [`examples/eeg_qc_demo.py`](../../examples/eeg_qc_demo.py). It demonstrates event markers, QC, epoching, ERP summaries, and frequency-domain analysis without reproducing participant data.
