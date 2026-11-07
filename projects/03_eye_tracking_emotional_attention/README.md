# Eye Tracking: Emotional Attention and Cross-Modal Distraction

**Evidence status:** PhD dissertation, OSF preregistered<br>
**Institution:** University of Arkansas, 2025<br>
**Preregistration:** https://doi.org/10.17605/OSF.IO/WK4M8

## Executive readout

**Problem:** Reaction time alone cannot distinguish early visual orienting, sustained gaze, oculomotor behavior, blinking, and pupil response.<br>
**Approach:** Build a 360-trial emotional-attention experiment synchronized with 1000 Hz EyeLink recording and three auditory conditions.<br>
**Result:** Angry faces delayed initial fixation relative to happy faces; smartphone notifications increased pupil variability relative to silence; several other endpoints were null or context dependent.

## My role

- Led the dissertation project end to end
- Designed the paradigm and study procedures
- Programmed and ran participant sessions
- Managed eye-tracking calibration and signal-quality procedures
- Analyzed fixation, saccade, blink, pupil, reaction-time, and accuracy endpoints
- Preregistered the study design and hypotheses

## Data / study scale

| Measure | Value |
|---|---:|
| Participants enrolled | 50 |
| EyeLink sample rate | 1000 Hz |
| Experimental trials | 360 per participant |
| Blocks | 6 x 60 |
| Emotional face pairs | 30 |

## Methods and technical implementation

EyeLink 1000 Plus, PsychoPy, EyeLink Data Viewer, R, calibration/validation, AOI and fixation analysis, saccades, blinks, pupil preprocessing, reaction time, accuracy, repeated-measures ANOVA, and mixed-effects models.

See [methods.md](methods.md) and [system_design.md](system_design.md).

## Results

The project identified endpoint-specific effects rather than a generalized distraction pattern. Initial fixation differed by emotional expression, pupil variability differed by sound condition, and several saccadic and behavioral outcomes were null.

See [results.md](results.md).

## What changed because of the result

The multimodal result localized effects to specific components of attention and physiology. That reduced reliance on a single reaction-time endpoint and strengthened the case for **measurement systems that distinguish orienting, gaze allocation, autonomic response, and behavior rather than treating them as interchangeable.**

## Limitations

- Endpoint-specific usable sample sizes after quality control
- Pupil values are relative/arbitrary units rather than calibrated millimeters
- Several hypothesized sound and saccade effects were not significant
- Participant-level gaze and licensed face stimuli are not publicly released

## Reproducibility / public artifacts

The public repeated-measures demonstration in [`examples/eye_tracking_metrics_demo.py`](../../examples/eye_tracking_metrics_demo.py) shows participant/trial QC and within-subject contrasts using synthetic data.
