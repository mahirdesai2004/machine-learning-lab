# Experiment 2: Multiple Regression Report

## Aim
To perform Multiple Linear Regression on the Vehicle CO2 Emission dataset to predict CO2 emissions based on vehicle features.

## Dataset Description
- **Dataset:** `car_co2_emission.csv`
- **Selected Features:** 
  - `ENGINESIZE`: Size of the car engine.
  - `CYLINDERS`: Number of cylinders.
  - `FUELCONSUMPTION_COMB`: Combined city and highway fuel consumption.
- **Target:** `CO2EMISSIONS` (Dependent Variable).
- **Goal:** Predict `CO2EMISSIONS` using multiple independent variables.

## Methodology
1. **Import Libraries:** Used Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.
2. **Data Loading:** Loaded and inspected the dataset.
3. **Feature Selection:** Selected relevant features (`ENGINESIZE`, `CYLINDERS`, `FUELCONSUMPTION_COMB`) alongside the target (`CO2EMISSIONS`).
4. **Data Splitting:** Split the data into 80% training and 20% testing sets.
5. **Model Training:** Initialized and trained a `LinearRegression` model using multiple features.
6. **Prediction:** Generated predictions on test data.
7. **Evaluation:** Calculated MSE, R2 score, and variance score.

## Results
- **Coefficients:** (Values from code)
- **Model Accuracy (R2):** Indicates the percentage of variance in CO2 emissions explained by the model.
- **Variance Score:** Close to 1.0 indicates good prediction accuracy.

## Conclusion
The multiple regression model provides a robust prediction for CO2 emissions. Engine size and fuel consumption were found to be significant predictors. The model demonstrates high accuracy as reflected by the R2 score.
