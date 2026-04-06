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
| **[Lab-06](./Lab-06/)** | K-Nearest Neighbour (KNN) & SVM Classification | Non-parametric modeling, High dimensional margins, Model generalization |
| **[Lab-07](./Lab-07/)** | Ensemble Learning (Bagging, Boosting, Stacking) | Variance reduction, Sequential error correction, Model aggregation |
| **[Lab-08](./Lab-08/)** | Clustering (K-Means & Hierarchical) | Unsupervised learning, Centroid-based partitioning, Dendrogram traversal |
| **[Lab-09](./Lab-09/)** | Artificial Neural Networks (ANN) | Deep Learning foundations, Multi-layer Perceptrons, Backward propagation |
| **[Lab-10](./Lab-10/)** | Convolutional Neural Networks (CNN) | spatial feature extraction, 1D Convolutions, Pooling strategies |
| **[Lab-11](./Lab-11/)** | Natural Language Processing (NLP) | Text Preprocessing, Tokenization, Stemming, Bag of Words, TF-IDF |
| **[Lab-12](./Lab-12/)** | Fraud Detection under Concept Drift (Project) | End-to-end classification pipeline, Imbalanced data, Threshold optimization, SHAP Explainability |

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

### 🟣 Lab-06: Non-Parametric & High Dimensional Supervised Learning
Evaluating distance-based vs margin-based models on the **Breast Cancer Wisconsin (Diagnostic)** dataset:
1. **K-Nearest Neighbour (KNN)** 🗺️
   - Evaluating localized distance-based classification to predict malignancy.
2. **Support Vector Machine (SVM)** ⚔️
   - Constructing optimal hyperplanes (linear kernel) for robust global margins.
3. **Comparative Analysis** ⚖️
   - Analyzing tradeoff sensitivity and overfitting susceptibility using ROC/AUC and localized heatmaps.

### 🟠 Lab-07: Ensemble Learning
Combining multiple classifiers on the **Breast Cancer Wisconsin (Diagnostic)** dataset:
1. **Bagging Classifier** 🎒
   - Reducing variance via bootstrap aggregation with Decision Trees.
2. **AdaBoost & Gradient Boosting** 🚀
   - Sequential error-correcting boosted classifiers.
3. **Stacking Classifier** 🏗️
   - Combining DT, KNN, and Logistic Regression with a meta-learner.
4. **Comparative Analysis** ⚖️
   - Four-way comparison of accuracy, ROC/AUC, and confusion matrices.

### 🟣 Lab-08: Unsupervised Learning (Clustering)
Implementing clustering algorithms on the **Iris** dataset:
1. **K-Means Clustering** 🧼
   - Grouping data into 'k' clusters with train-test (80:20) splits.
   - Evaluated using average Silhouette Scores and mapped Accuracy.
2. **Hierarchical Clustering** 🌲
   - Building a tree of clusters using Agglomerative strategies.
   - Visualizing data relationships with Dendrograms.
3. **Comparative Analysis** ⚖️
   - Bar chart comparison of Accuracy and Silhouette scores.
   - Analyzing side-by-side Confusion Matrices for cluster alignment.

### 🟠 Lab-09: Artificial Neural Networks (ANN)
Implementing foundational Deep Learning models on the **Iris** dataset:
1. **Multi-Layer Perceptron (MLP)** 🧠
   - Constructing an ANN with multiple hidden layers using `MLPClassifier`.
   - Iterative weight optimization via backpropagation.
2. **Performance Evaluation** ⚖️
   - Analysis of Accuracy, Precision, and Recall on scaled feature sets.
   - Visualization of the Training Loss curve to monitor convergence.

### 🔴 Lab-10: Convolutional Neural Networks (CNN)
Designing spatial feature extraction models for sequence/tabular data:
1. **1D Convolutional Neural Network** 💠
   - Building a 1D CNN using `TensorFlow/Keras` to identify Iris patterns.
   - Implementing Conv1D, MaxPooling, and Dense layers.
2. **Evaluation and Training History** ⚖️
   - Monitoring training loops with Accuracy and Loss plots over epochs.
   - final model validation using high-precision evaluation metrics.

### 🟡 Lab-11: Natural Language Processing (NLP)
Implementing fundamental Natural Language Processing techniques:
1. **Text Preprocessing & Normalization** 📝
   - Cleaning and tokenizing raw text streams using `nltk`.
   - Applying Stemming (PorterStemmer) and Lemmatization (WordNetLemmatizer) to extract term derivations.
2. **Text Representation & Vectorization** 🧮
   - Generating standard token frequency matrices with Bag of Words (`CountVectorizer`).
   - Extracting domain-relevant feature weights with `TfidfVectorizer`.

### 🟤 Lab-12: Fraud Detection under Concept Drift (Project)
End-to-end production pipeline addressing highly imbalanced data (~1.5% fraud rate):
1. **Model Optimization** ⚙️
   - Training extreme gradient boosting (`XGBoost`) models with temporal cross-validation.
   - Cost-sensitive classification using optimized threshold sweeping.
2. **Evaluation and Explainability** ⚖️
   - Maximizing PR-AUC (Precision-Recall Area) over traditional ROC-AUC.
   - Utilizing SHAP summaries to explain specific feature contributions.

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
