# Machine Learning Lab - 04 🚀

Welcome to the **Machine Learning Lab-04** repository! This project demonstrates the implementation of fundamental Regression and Classification algorithms using Python and Scikit-learn.

## 📂 Repository Structure

The repository is organized into three main experiments:

```
📦 Machine-Learning-Lab
 ┣ 📂 Experiment-1-Linear-Regression
 ┃ ┣ 📜 notebook.ipynb       # Simple Linear Regression implementation
 ┃ ┣ 📜 report.md            # Detailed report of Exp 1
 ┃ ┗ 📜 sales_tv_marketing.csv
 ┣ 📂 Experiment-2-Multiple-Regression
 ┃ ┣ 📜 notebook.ipynb       # Multiple Linear Regression with Visualizations
 ┃ ┣ 📜 report.md            # Detailed report of Exp 2
 ┃ ┗ 📜 car_co2_emission.csv
 ┗ 📂 Experiment-3-Logistic-Regression
   ┣ 📜 notebook.ipynb       # Logistic Regression (Refined)
   ┣ 📜 report.md            # Detailed report of Exp 3
   ┗ 📜 ad_click_prediction.csv
```

---

## 🔬 Experiments Overview

### 1️⃣ Experiment 1: Simple Linear Regression
**Objective:** Predict Sales based on TV Marketing budget.
- **Model:** Simple Linear Regression ($y = mx + c$)
- **Dataset:** `sales_tv_marketing.csv`
- **Key Metrics:** $R^2$ Score, Mean Squared Error (MSE)

### 2️⃣ Experiment 2: Multiple Linear Regression
**Objective:** Predict CO2 Emissions of vehicles based on features like Engine Size, Cylinders, and Fuel Consumption.
- **Model:** Multiple Linear Regression
- **Dataset:** `car_co2_emission.csv`
- **Highlights:**
  - 📊 Correlation Heatmap
  - 📦 Outlier Detection (Box Plots)
  - 📉 Scatter Plots for Feature Relations

### 3️⃣ Experiment 3: Logistic Regression
**Objective:** Predict whether a user will click on an online advertisement.
- **Model:** Logistic Regression (Binary Classification)
- **Dataset:** `ad_click_prediction.csv`
- **Key Features:**
  - 🧹 **EDA:** Missing value treatment, Data Normalization.
  - 🕒 **Feature Engineering:** Extracted 'Hour' from Timestamp to analyze time-of-day impact.
  - 📈 **Evaluation:**
    - Confusion Matrix
    - ROC Curve & AUC
    - Precision-Recall Curve
    - K-Fold Cross Validation

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Pandas** & **NumPy** (Data Manipulation)
- **Matplotlib** & **Seaborn** (Visualization)
- **Scikit-learn** (Machine Learning Models)
- **Jupyter Notebook** (Interactive Coding)

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/mahirdesai2004/machine-learning-lab.git
   ```
2. Navigate to the experiment folder:
   ```bash
   cd machine-learning-lab/Lab-04/Experiment-1-Linear-Regression
   ```
3. Open the notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

---
*Created by [Mahir Desai](https://github.com/mahirdesai2004)*
