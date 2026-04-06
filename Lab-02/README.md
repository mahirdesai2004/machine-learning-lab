# 🟡 ML Lab 02 – Data Preprocessing and Visualization

This directory addresses essential steps for data cleaning, prep, and visual analytics, which are precursors to robust machine learning models.

## 📝 Objective
Master data verification methods, handle missing/anomalous variables, and execute plotting functions to uncover dataset behavior. 

## 📂 Structure
- `notebook.ipynb` - Pipeline establishing missing value injections, Pandas data cleansing workflows, and feature graphs.
- `ML LAB -2.docx` - Lab report featuring theoretical discussions, source code, and Matplotlib integration.
- `outputs/` - Images summarizing data layout:
    - Bar and Line charts showing instance distribution.
    - Scatter plots evaluating positive/negative variable correlation.
    - Histograms for skewness examination.
    - Box plots for visual outlier detection.

## 🧪 Experiments Covered
1. **Evaluating Null Configurations**: Locating missing records across diverse variables.
2. **Missing Deletion Methods**: Observing frame integrity when eliminating unpopulated rows via `dropna()`.
3. **Imputation Methods**: Recovering integrity by estimating missing entries using column aggregations (`fillna(mean)`).
4. **Data Casts**: Optimizing dataframe footprint with memory-appropriate column bounds using `astype`.
5. **Column Modification**: Utilizing target naming updates with `rename()`.
6. **Value Discrepancy Rectification**: Utilizing exact targeting via `replace()` to mend logical outliers.
7. **Bar & Line Graphs**: Simple plots for comparative counts and trends mapping over arbitrary sequential ranges.
8. **Relational Geometry (Scatter)**: Assessing multi-variable dependencies (e.g. Petal size).
9. **Volumetric Data Analysis (Histograms)**: Determining statistical uniformity and distribution mass.
10. **Quartile Plots (Boxplots)**: Uncovering extreme distribution shifts beyond bounds with Whiskers.
