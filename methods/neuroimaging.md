# Secondary fMRI / Neuroimaging Analysis

## Portfolio use case

ABCD secondary analysis of screen time, caregiver warmth, and BOLD activity during the Monetary Incentive Delay task.

## Processing and modeling decisions

- Analytic sample: 1,119 youth
- Nucleus accumbens and anterior insula regions of interest
- Exclusion for MRI motion greater than 3 mm/s
- Exclusion of extreme BOLD beta values greater than 3 SD
- Screen time aggregated across digital-media categories and log transformed
- Caregiver warmth measured with the Acceptance Scale and transformed for skew
- Model: `ROI activity ~ screen time * caregiver warmth`
- Analysis implemented in R/RStudio with RMarkdown

## Interpretation principle

A statistically significant coefficient is not equivalent to strong explanatory power. The right anterior-insula model had a significant screen-time x warmth interaction while explaining less than 1% of variance after adjustment. The portfolio therefore reports the result as a small observational association.
