# 🟣 ML Lab 08 – Unsupervised Learning (Clustering)

This directory contains the implementation of unsupervised learning techniques using the Iris dataset. It follows the high-standard comparison structure established in previous labs, including train-test splits and performance bar charts.

## 📝 Objective
Build and compare **K-Means Clustering** and **Agglomerative Hierarchical Clustering** on the Iris dataset. The evaluation includes mapping clusters to labels to calculate accuracy, alongside traditional silhouette analysis.

## 📂 Structure
- `notebook.ipynb` - Step-by-step experiment with train-test split (80:20).
- `ML LAB -8.docx` - Formal report with code, outputs, and embedded plots.
- `outputs/` - Generated assets:
    - `dendrogram.png`: Hierarchy visualization.
    - `accuracy_comparison_8.png`: Bar chart comparing models.
    - `confusion_matrices_8.png`: Cluster-to-label alignment heatmaps.

## 📊 Evaluation Metrics
- **K-Means Accuracy**: ~90% (mapped)
- **Hierarchical Accuracy**: ~87% (mapped)
- **Silhouette Scores**: ~0.44 - 0.45
- **Dendrogram**: Visual representation of hierarchical distance.

## 🏆 Key Observations
- K-Means produced clusters more consistent with the underlying Iris species labels.
- Scaling was critical for consistent distance calculations between features.
- The comparative bar charts clearly demonstrate the trade-offs between centroid-based and connectivity-based algorithms.
