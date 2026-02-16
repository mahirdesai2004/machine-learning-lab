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

### 4. Results
- **Model Coefficients**: The coefficients for Engine Size, Cylinders, and Fuel Consumption indicate their relative impact on CO2 emissions.
- **Model Accuracy**:
    - **Mean Squared Error (MSE)**: Calculated to evaluate the average squared difference between estimated values and the actual value.
    - **R-squared ($R^2$)**: A statistical measure that represents the proportion of the variance for a dependent variable that's explained by an independent variable or variables in a regression model.
- **Visualizations**:
    - **Correlation Heatmap**: Displayed strong positive correlations between Engine Size, Cylinders, Fuel Consumption, and CO2 Emissions, indicating these are strong predictors.
    - **Outlier Detection**: Box plots revealed potential outliers in Fuel Consumption and CO2 Emissions, which may affect model performance.
    - **Scatter Plots**: Confirmed linear relationships between CO2 and the selected features, satisfying the linearity assumption of OLS regression.

## Conclusion
The Multiple Linear Regression model successfully predicted CO2 emissions based on vehicle features. The high $R^2$ score and low MSE indicate a good fit. The additional visualizations provided deeper insights:
1.  **Correlation**: Strong positive correlation among features suggests multicollinearity might be present, but they are all strong predictors of CO2.
2.  **Outliers**: Presence of outliers suggests robust regression techniques or data cleaning might further improve the model.
3.  **Linearity**: Scatter plots confirmed the linear relationship assumption.
Overall, the model is effective for estimating CO2 emissions from vehicle characteristics. The model demonstrates high accuracy as reflected by the R2 score.
