# 🔴 ML Lab 10 – Convolutional Neural Networks (CNN)

This directory contains the implementation of a 1D Convolutional Neural Network (CNN) for classification on the Iris dataset.

## 📝 Objective
Design and implement a CNN model using TensorFlow/Keras to classify species of Iris. The experiment demonstrates how convolution and pooling layers can be applied to 1D feature vectors to extract meaningful spatial patterns.

## 📂 Structure
- `notebook.ipynb` - Chronological implementation covering data reshaping, CNN architecture, and training history.
- `ML LAB -10.docx` - Professional lab report with embedded training logs and performance charts.
- `outputs/` - Visual results:
    - `training_history.png`: Plots for Accuracy and Loss over 50 epochs.
    - `confusion_matrix.png`: Prediction accuracy heatmap.

## 📊 Performance Metrics
- **Accuracy**: 100% (Robust convergence within 50 epochs)
- **Architecture**: Conv1D (32 filters) → MaxPooling1D → Flatten → Dense (16) → Output (3, Softmax)
- **Optimizer**: Adam

## 🏆 Key Observations
- 1D Convolutions are highly effective at capturing local dependencies even in small tabular datasets like Iris.
- Reshaping the data to `(samples, 4, 1)` is a necessary architectural step for CNN compatibility.
- The use of MaxPooling helps in generalizing features and reducing the parameter space.
