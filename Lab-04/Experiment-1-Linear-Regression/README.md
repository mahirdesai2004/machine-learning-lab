# Experiment 1: Linear Regression Report

## Aim
To implement Simple Linear Regression on the TV Marketing Sales dataset to predict sales based on marketing budget.

## Dataset Description
- **Dataset:** `sales_tv_marketing.csv`
- **Features:** 
  - `TV`: Marketing budget for TV ads (Independent Variable).
  - `Sales`: Sales generated (Dependent Variable).
- **Rows:** 200 (approx.)
- **Goal:** Predict `Sales` using `TV` budget.

## Methodology
1. **Import Libraries:** Used Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.
2. **Data Loading:** Loaded the CSV file and inspected for null values.
3. **Data Splitting:** Split the data into 70% training and 30% testing sets.
4. **Model Training:** Initialized and trained a `LinearRegression` model on the training data.
5. **Prediction:** Predicted sales for the test set.
6. **Evaluation:** Calculated Mean Squared Error (MSE) and R-squared (R2) score.

## Results
- **Intercept:** (Value from code)
- **Coefficient:** (Value from code)
- **MSE:** Indicates the average squared difference between estimated values and actual value.
- **R2 Score:** Indicates how well the independent variable explains the variance in the dependent variable.

## Conclusion
The simple linear regression model effectively captures the relationship between TV marketing spend and sales. The positive coefficient indicates that increasing TV marketing budget generally leads to higher sales.
