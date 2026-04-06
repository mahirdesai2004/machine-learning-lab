# 🟢 ML Lab 03 – Descriptive Statistical Analysis

This directory explores fundamental statistical computations necessary for understanding the underlying distribution of raw data before passing it to complex machine learning pipelines.

## 📝 Objective
Apply statistical methodology to define the center, spread, scaling, and mutual dependencies amongst the dataset variables using standard mathematics implementations inside Scikit/Pandas operations.

## 📂 Structure
- `notebook.ipynb` - The primary processing code reading academic profiles to determine aggregate mathematical patterns.
- `ML LAB -3.docx` - Lab report showing numeric data interpretations and visual verifications.
- `outputs/` - Images summarizing data layouts:
    - `histograms.png`: Data count bins mapped to bell-curve densities.
    - `boxplots.png`: Uncovering density percentiles and strict outliers.

## 🧪 Experiments Covered
1. **Central Tendencies**: Generating exact Mean, Median, and Mode for all continuous attributes. Generating dispersion mapping via variance and deviations.
2. **Quartile Separation**: Identifying identical Q1 (25th), Q2 (Median), and Q3 (75th) data blocks, plus the Interquartile Range (IQR).
3. **Correlation Tracking**: Identifying linked columns utilizing exactly bound `-1 to 1` mapping coefficients via `corr()`. Computing Covariance arrays for unbound structural tracking.
4. **Distribution Visualization**: Establishing multi-layout figure bounds yielding visual interpretations of statistical data skews and IQR visual outlier clipping.
