<div align="center">
  <h1>🧠 Machine Learning Lab Implementations</h1>
  <p><i>A structured repository containing Machine Learning algorithms implemented using Python, Pandas, and Scikit-Learn.</i></p>

  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    <img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white" />
    <img src="https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white" />
    <img src="https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white" />
    <img src="https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black" />
  </p>
</div>

---

## 📌 Repository Overview

This repository serves as a centralized collection my comprehensive Machine Learning experiments. Every experiment focuses on a core ML concept ranging from simple regressions to complex classification tree models, fully documented with exploratory data analysis (EDA), model training, evaluation, and visualizations.

---

## 📂 Directories

| Lab | Experiments | Core Technologies |
|---|---|---|
| **[Lab-04](./Lab-04/)** | Simple Linear, Multiple Linear, & Logistic Regression | `scikit-learn`, Binary Classification, Evaluation Metrics |
| **[Lab-05](./Lab-05/)** | Naïve Bayes & Decision Tree Classification | Multi-class datasets, Precision-Recall, ROC Curves, Cost-Complexity |

---

## 🔬 Experiment Details

### 🟢 Lab-04: Regression Models
Three robust implementations exploring continuous and binary target prediction:
1. **Simple Linear Regression** 📈
   - Forecasting Sales based on TV Marketing budget.
2. **Multiple Linear Regression** 🚗
   - Predicting CO2 emissions using multivariate feature analysis (Engine Size, Cylinders).
   - In-depth collinearity checks with Heatmaps and Box Plot outlier detection.
3. **Logistic Regression** 🖱️
   - Binary classification to predict online advertisement click-through rates.
   - Comprehensive EDA, feature engineering, and K-Fold cross-validation.

### 🔵 Lab-05: Supervised Learning (Classification)
Comparing probabilistic and rule-based prediction models on the **Breast Cancer Wisconsin (Diagnostic)** dataset:
1. **Naïve Bayes Classifier** 📐
   - Building a Gaussian NB model to evaluate high-bias probabilistic calculations.
2. **Decision Tree Classifier** 🌳
   - Gini-impurity based decision rules visualization (`plot_tree`).
3. **Comparative Analysis** ⚖️
   - Direct comparison of generalization utilizing precision, recall, confusion matrix heatmaps, and consolidated ROC curves.

---

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mahirdesai2004/machine-learning-lab.git
   cd machine-learning-lab
   ```

2. **Navigate to an experiment and launch Jupyter:**
   ```bash
   cd Lab-05
   jupyter notebook notebook.ipynb
   ```

3. **Install dependencies:**
   Ensure you have the required Python packages:
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

---

<div align="center">
  <i>Maintained by <a href="https://github.com/mahirdesai2004">Mahir Desai</a></i>
</div>
