# 🟣 ML Lab 08 – Clustering (K-Means & Hierarchical)

This directory contains the implementations for Lab 8, focusing on unsupervised learning techniques (K-Means and Hierarchical Clustering) applied to the Iris dataset using Scikit-Learn.

## 📝 Objective
Build, evaluate, and compare **K-Means Clustering** and **Agglomerative Hierarchical Clustering**. The goal is to understand how unsupervised algorithms group data without prior labels and how to evaluate them using silhouette scores.

## 📂 Structure
- `notebook.ipynb` - The primary Jupyter Notebook with step-by-step experiments.
- `ML LAB -8.docx` - The formalized lab report document.
- `outputs/` - Generated visualization assets (Dendrogram, Cluster Comparison plot).

## 📊 Evaluation Metrics Computed
- Silhouette Coefficient (for both K-Means and Hierarchical)
- Dendrogram Visualization (Scipy)
- Cluster Distribution Scatter Plots (Seaborn)

## 🏆 Key Results
- Both models efficiently grouped the Iris data into three distinct species.
- **K-Means** showed a slightly higher silhouette score (~0.445) compared to **Hierarchical** (~0.441) on the scaled Iris dataset.
- The **Dendrogram** successfully visualized the hierarchical relationship between different samples.
