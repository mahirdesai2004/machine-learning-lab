# Experiment 3: Logistic Regression Report

## Aim
To implement Logistic Regression on the Ad Click Prediction dataset to classify whether a user will click on an advertisement based on user features.

## Dataset Description
- **Dataset:** `ad_click_prediction.csv`
- **Features Used:** 
  - `Daily Time Spent on Site`
  - `Age`
  - `Area Income`
  - `Daily Internet Usage`
  - `Male` (Gender flag)
- **Target:** `Clicked on Ad` (0 = No, 1 = Yes)
- **Goal:** Binary classification of ad clicks.

### 3. Methodology
1. **Data Loading:** Load the `ad_click_prediction.csv` dataset.
2. **Exploratory Data Analysis (EDA):**
    - Check for missing values and outliers.
    - Visualize correlation using a Heatmap.
3. **Data Preprocessing:**
    - **Feature Engineering:** Extract 'Hour' from 'Timestamp' to capture time-of-day effects.
    - **Dropping Features:** Remove high-cardinality text features like 'Ad Topic Line', 'City', and 'Country'.
    - **Normalization:** Scale numerical features using `StandardScaler`.
4. **Model Training:**
    - Split data into training and testing sets (80:20).
    - Train a Logistic Regression model.
5. **Cross-Validation:** Perform 10-Fold Cross-Validation to assess model stability.
6. **Evaluation:**
    - Generate Classification Report (Precision, Recall, F1-score).
    - Plot Confusion Matrix.
    - Plot ROC Curve and calculate AUC.
    - Plot Precision-Recall Curve.
    - Visualize Predicted vs Actual outcomes.

### 4. Results
- **Model Accuracy:** The model achieves high accuracy in predicting ad clicks.
- **Cross-Validation:** K-Fold CV results demonstrate the model's consistency across different data subsets.
- **ROC/AUC:** The Receiver Operating Characteristic curve and Area Under Curve (AUC) score indicate strong discriminatory power between clicked and non-clicked instances.
- **Confusion Matrix:** Shows the breakdown of True Positives, True Negatives, False Positives, and False Negatives.

## Conclusion
The Logistic Regression model effectively predicts user interaction with online ads based on demographics and browsing behavior. Feature engineering (extracting time information) and normalization contributed to the model's performance. The comprehensive evaluation using ROC and Precision-Recall curves confirms the model's reliability for this binary classification task.
