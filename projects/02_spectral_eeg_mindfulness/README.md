# Spectral EEG: Notifications, Mindfulness, and Cognitive Control

**Evidence status:** Peer-reviewed, first and corresponding author  
**Publication:** *Biological Psychology* (2023), 185, 108725  
**DOI:** https://doi.org/10.1016/j.biopsycho.2023.108725

## Executive readout

**Problem:** ERP peaks capture time-locked responses but do not fully characterize oscillatory neural dynamics during distraction.  
**Approach:** Extend the notification paradigm to theta, alpha, beta, and theta/beta-ratio measures after randomized mindfulness vs neutral narration.  
**Result:** Notifications altered task-locked spectral power and selected mindfulness-related contrasts emerged, but the omnibus group x sound TBR interaction was not significant. The interpretation was therefore deliberately bounded.

## Study scale

| Measure | Value |
|---|---:|
| Eligible participants | 101 |
| EEG datasets before preprocessing | 97 |
| Final EEG sample | 87 |
| Mindfulness / control | 44 / 43 |
| EEG channels | 32 active electrodes |
| Acquisition rate | 512 Hz |

## Technical stack

BioSemi ActiveTwo, MATLAB, EEGLAB, artifact subspace reconstruction, extended Infomax ICA, ICLabel, event-locked epochs, theta/alpha/beta spectral analyses, theta/beta ratio, repeated-measures inference.

See [methods.md](methods.md), [results.md](results.md), and [technical_notes.md](technical_notes.md).
