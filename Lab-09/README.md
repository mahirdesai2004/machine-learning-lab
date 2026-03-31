# 🟠 ML Lab 09 – Artificial Neural Networks (ANN)

This directory contains the implementation of a Multi-Layer Perceptron (MLP) Artificial Neural Network for classifying the Iris species.

## 📝 Objective
Implement a basic ANN using Scikit-Learn's `MLPClassifier` and evaluate its performance. The experiment explores the impact of feature scaling, hidden layer configurations, and convergence metrics.

## 📂 Structure
- `notebook.ipynb` - Step-by-step implementation from data preprocessing to model visualization.
- `ML LAB -9.docx` - Formalized lab report document.
- `outputs/` - Visual assets including the Confusion Matrix heatmap and Training Loss curve.

## 📊 Performance Metrics
- **Accuracy**: 100% (High performance on scaled Iris dataset)
- **Model Architecture**: Input Layer (4) → Hidden Layer 1 (10) → Hidden Layer 2 (8) → Output Layer (3)
- **Activation**: ReLU (default for MLPClassifier)

## 🏆 Key Observations
- Feature scaling is essential for ANNs to prevent gradient divergence.
- The model converges rapidly on the Iris dataset, achieving perfect classification on the test set.
- The loss curve shows smooth minimization of categorical cross-entropy over iterations.
