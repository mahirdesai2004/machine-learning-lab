# 🟣 ML Lab 06 – Non-Parametric & High Dimensional Supervised Learning

This directory contains the implementations for Lab 6, focusing on K-Nearest Neighbours (KNN) and Support Vector Machines (SVM) for binary classification on the Breast Cancer dataset using Scikit-Learn.

## 📝 Objective
Build, evaluate, and compare **K-Nearest Neighbour (KNN)** and **Support Vector Machine (SVM)** classification models. The goal is to determine the optimal model for medical diagnosis emphasizing high Recall to minimize life-threatening false negatives.

## 📂 Structure
- `notebook.ipynb` - The primary Jupyter Notebook containing step-by-step experiment implementations, code, and markdown answers.
- `ML LAB -6.docx` - The formalized lab report document, formatted cleanly for submission.
- `ML Lab-6.pdf` - The original assignment criteria.
- `outputs/` - Generated visualization assets (ROC curves, Confusion Matrix heatmaps).

## 📊 Evaluation Metrics Computed
- Overall Accuracy
- Confusion Matrix Heatmaps (Seaborn)
- Classification Reports (Precision, Recall, F1-Score)
- Precision-Recall Curves
- Area Under ROC Curve (AUC)

## 🏆 Key Results
Both **SVM (Linear Kernel)** and **KNN (k=5)** achieved high testing accuracy (95.61%). However, **SVM demonstrated superior recall** (91% vs 88%) for critical malignant cancer cases. Because medical diagnosis heavily penalizes missing a true positive, SVM proved to be the more suitable, better-generalizing model for this specific dataset.
