# 🔵 ML Lab 05 – Supervised Learning (Classification)

This directory contains the implementations for Lab 5, focusing on binary classification of medical diagnostics using Scikit-Learn.

## 📝 Objective
Build, evaluate, and compare **Naïve Bayes** and **Decision Tree** classification models using the **Breast Cancer Wisconsin Diagnostic dataset**. The goal is to determine the optimal model for medical diagnosis where minimizing false negatives (maximizing Recall) is critical.

## 📂 Structure
- `notebook.ipynb` - The primary Jupyter Notebook containing step-by-step experiment implementations, code, and markdown answers.
- `ML LAB -5.docx` - The formalized lab report document, formatted cleanly for submission.
- `ML_LAB_5.pdf` - The original assignment criteria.
- `outputs/` - Generated visualization assets (ROC curves, Decision Tree graphs, Heatmaps).

## 📊 Evaluation Metrics Computed
- Overall Accuracy
- Confusion Matrix Heatmaps (Seaborn)
- Classification Reports (Precision, Recall, F1-Score)
- Precision-Recall Curves
- Area Under ROC Curve (AUC)

## 🏆 Key Results
**Naïve Bayes** ultimately achieved a higher overall testing accuracy (97.37%) and demonstrated **superior recall** (93%) for malignant cancer cases compared to the Decision Tree. Because medical diagnosis heavily penalizes missing a true positive, Naïve Bayes proved to be the more suitable, better-generalizing model for this specific dataset.
