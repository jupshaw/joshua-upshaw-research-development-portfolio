# Methods

## Design

Participants were randomized to a brief mindfulness induction or neutral narration control, then completed a local-global task in which smartphone notification, control tone, and silence conditions were interleaved.

## Acquisition and preprocessing

- 32 active EEG electrodes with BioSemi ActiveTwo
- 512 Hz acquisition; later downsampled to 256 Hz
- Vertical and horizontal EOG
- Filtering and line-noise handling
- Bad-channel interpolation
- Common-average rereferencing
- Artifact subspace reconstruction
- Extended Infomax ICA
- ICLabel classification of non-brain components
- 35 Hz low-pass filtering
- Event labels and stimulus-locked epochs

## Spectral definitions

- Theta: 4-7 Hz
- Alpha: 8-12 Hz
- Beta: 13-30 Hz
- Theta/beta ratio as an additional composite measure

## Quality-control lesson

Peer review identified a reporting error in the initially transcribed ICA-component statistic. The final corrected manuscript reports an average of **2.73 (SD 2.08)** components flagged per participant and no group difference in component rejection, `t(85) = 0.06, p = .951`. The correction is retained in this portfolio because error detection and transparent correction are part of scientific rigor.
