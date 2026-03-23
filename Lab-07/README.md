# 🟠 ML Lab 07 – Ensemble Learning (Bagging, Boosting, Stacking)

This directory contains the implementations for Lab 7, focusing on ensemble classification techniques applied to the Breast Cancer dataset using Scikit-Learn.

## 📝 Objective
Build, evaluate, and compare **Bagging**, **AdaBoost**, **Gradient Boosting**, and **Stacking** classification models. The goal is to understand how ensemble strategies improve upon individual classifiers.

## 📂 Structure
- `notebook.ipynb` - The primary Jupyter Notebook with step-by-step experiments.
- `ML LAB -7.docx` - The formalized lab report document.
- `outputs/` - Generated visualization assets (ROC curves, Confusion Matrices, Accuracy charts).

## 📊 Evaluation Metrics Computed
- Overall Accuracy
- Confusion Matrix Heatmaps (Seaborn)
- Classification Reports (Precision, Recall, F1-Score)
- Precision-Recall Curves
- Area Under ROC Curve (AUC)

## 🏆 Key Results
**AdaBoost** and **Stacking** achieved the highest testing accuracy. Boosting models demonstrated consistently strong recall for malignant cases, making them preferable for medical diagnosis scenarios where minimizing false negatives is critical.
