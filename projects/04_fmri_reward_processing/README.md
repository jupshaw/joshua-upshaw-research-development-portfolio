# fMRI: Screen Time, Caregiver Warmth, and Reward/Risk Processing

**Evidence status:** Graduate neuroimaging course project, 2024; not peer reviewed  
**Dataset:** Adolescent Brain Cognitive Development (ABCD) secondary analysis

## Executive readout

**Problem:** Screen time may covary with developing reward/risk circuitry, but environmental context could modify that relationship.  
**Approach:** Test screen time x caregiver-warmth interactions in predefined NAcc and anterior-insula BOLD measures during the Monetary Incentive Delay task.  
**Result:** A right anterior-insula interaction reached significance, but adjusted R2 was only 0.0073. The effect is therefore reported as a small observational association rather than a strong explanatory model.

## My role

- Completed the secondary neuroimaging analysis as a graduate research project
- Defined the moderation models and region-of-interest comparisons
- Implemented reproducible analysis in R/RMarkdown
- Interpreted statistical significance alongside explained variance and design limitations

## Data / study scale

| Measure | Value |
|---|---:|
| Analytic sample | 1,119 youth |
| Task | Monetary Incentive Delay |
| ROIs | Nucleus accumbens, anterior insula |
| Analysis | Multiple linear regression with interaction |
| Environment | R, RStudio, RMarkdown |

## Methods and technical implementation

ABCD secondary data, MID task ROI BOLD measures, regression with interaction terms, transformed predictors, motion/outlier controls, and reproducible RMarkdown reporting.

See [methods.md](methods.md).

## Results

The right anterior-insula screen-time x warmth interaction met the conventional significance threshold, but the model explained very little variance. The NAcc interaction was not significant.

See [results.md](results.md).

## What changed because of the result

The project reinforced that **statistical significance and explanatory usefulness are different questions**. A significant coefficient with adjusted R2 = 0.0073 is appropriate for hypothesis generation, not a strong mechanistic or developmental claim.

## Limitations

- Observational secondary analysis
- Very small explained variance
- No causal inference
- Course project, not peer reviewed

## Reproducibility / public artifacts

Public portfolio materials document the model structure and interpretation. Restricted ABCD participant-level data are not redistributed.
