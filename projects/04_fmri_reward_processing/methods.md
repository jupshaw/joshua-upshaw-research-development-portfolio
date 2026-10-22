# Methods

## Sample

The analysis used 1,119 ABCD participants with completed youth mobile-technology and caregiver-behavior measures. The source project describes matching/selection intended to reduce developmental variability.

## Predictors

- Youth screen time aggregated across multiple digital-media categories and log transformed
- Caregiver warmth measured with the Child Report of Behavior Inventory Acceptance Scale and transformed for skew

## Neuroimaging outcome

ROI-level BOLD measures during Monetary Incentive Delay contrasts in the nucleus accumbens and anterior insula.

## Quality gates

- MRI motion greater than 3 mm/s excluded
- Extreme BOLD beta values greater than 3 SD excluded

## Model

```r
lm(ROI_activity ~ screen_time_log * caregiver_warmth_transformed, data = analysis_df)
```

A synthetic RMarkdown demonstration is included as [`analysis_example.Rmd`](analysis_example.Rmd).
