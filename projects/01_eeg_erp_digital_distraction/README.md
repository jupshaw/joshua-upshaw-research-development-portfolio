# EEG/ERP: Smartphone Notifications and Cognitive Control

**Evidence status:** Peer-reviewed, first-author research<br>
**Publication:** *PLOS ONE* (2022)<br>
**DOI:** https://doi.org/10.1371/journal.pone.0277220

## Executive readout

**Problem:** Smartphone notification sounds are ecologically familiar distractors, but behavior alone cannot identify which processing stage changes.<br>
**Approach:** Pair notification/control sounds with a local-global visual oddball task while recording EEG and behavior.<br>
**Result:** Smartphone trials were slightly slower and N2 amplitude differed by sound condition, while P3 and several moderation effects did not. The evidence supports a selective, modest neural effect rather than a broad impairment claim.

## My role

- Designed and executed attention / notification experiments within the doctoral research program
- Acquired and analyzed EEG and behavioral data
- Evaluated P2/N2/P3 components and reaction-time/accuracy outcomes
- Applied event synchronization and signal-quality controls
- Translated findings into a first-author peer-reviewed publication

## Data / study scale

| Measure | Value |
|---|---:|
| Participants recruited | 73 |
| Final behavioral sample | 69 |
| Final ERP sample | 54 |
| Task design | 960 trials per participant |
| Trial-level RT observations reported | 37,769 |

## Methods and technical implementation

BioSemi EEG, MATLAB, EEGLAB, ICA, ICLabel, ERP analysis, local-global Navon oddball task, event synchronization, trial-level regression, reaction time, and accuracy analysis.

See [methods.md](methods.md) and [reproducibility.md](reproducibility.md).

## Results

The study identified small behavioral slowing on smartphone-notification trials and selective N2 differences, while P3 and multiple moderation effects were null. The interpretation was therefore limited to the specific neural and behavioral processes supported by the data.

See [results.md](results.md).

## What changed because of the result

The findings shifted the research program away from a simple "notifications impair cognition" framing toward a more specific question: **which attentional and control processes are affected, under which task demands, and in whom?** That motivated later spectral EEG and eye-tracking work using complementary measures.

## Limitations

- ERP sample reduced after technical/artifact exclusions
- Several hypothesized moderation effects were not supported
- Undergraduate sample limits generalizability
- Observed effects were modest and should not be generalized to all forms of digital distraction

## Reproducibility / public artifacts

Participant-level EEG is not released here. Public materials document methods, results, and a synthetic event-based EEG demonstration in [`examples/eeg_qc_demo.py`](../../examples/eeg_qc_demo.py).
