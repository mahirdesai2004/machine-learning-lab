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

## Methodology
1. **Import Libraries:** Used Pandas, NumPy, Matplotlib, Seaborn, and Scikit-learn.
2. **Data Loading:** Loaded the dataset.
3. **Data Visualization:** Plotted correlation heatmap and pairplot to understand feature relationships.
4. **Data Preprocessing:** Selected numerical features and split data (70% train, 30% test).
5. **Model Training:** Initialize `LogisticRegression` and trained on the training set.
6. **Prediction:** Predicted outcomes on the test set.
7. **Evaluation:** Generated Confusion Matrix, Accuracy Score, and Classification Report.

## Results
- **Confusion Matrix:** Shows True Positives, True Negatives, False Positives, and False Negatives.
- **Accuracy:** The percentage of correct predictions.
- **Classification Report:** Precision, Recall, and F1-score for each class.

## Conclusion
The Logistic Regression model effectively classifies users likely to click on an ad. The evaluation metrics (Accuracy, Precision, Recall) confirm its suitability for this binary classification task.
