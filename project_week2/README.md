# Project 3: Heart Disease Risk Assessment using Tree-Based Models

## Overview

This project predicts the presence of heart disease using two Machine Learning classification algorithms:

- Decision Tree Classifier
- Random Forest Classifier

The project also analyzes **feature importance** to determine which medical factors contribute the most to heart disease prediction.

---

## Objectives

- Load and preprocess the Heart Disease dataset.
- Handle missing values.
- Convert categorical data into numerical format.
- Train a Decision Tree classifier.
- Train a Random Forest classifier.
- Compare the performance of both models.
- Visualize the Decision Tree.
- Display Feature Importance using Random Forest.
- Identify the most and least important features.

---

## Dataset

**Dataset Name:** UCI Heart Disease Dataset

Dataset File:

```
heart_disease_uci.csv
```

Target Variable:

```
num
```

Target Values:

- 0 → No Heart Disease
- 1 → Heart Disease

---

## Technologies Used

- Python
- Pandas
- Matplotlib
- Scikit-learn

---

## Libraries Required

Install the required libraries using:

```bash
pip install pandas matplotlib scikit-learn
```

---

## Project Workflow

### Step 1

Load the Heart Disease dataset.

### Step 2

Remove unnecessary columns:

- id
- dataset

### Step 3

Convert the target variable:

```
0 → No Disease
1 → Disease
```

### Step 4

Convert categorical variables using One-Hot Encoding.

### Step 5

Handle missing values using SimpleImputer.

### Step 6

Split the dataset into Training and Testing sets.

### Step 7

Train a Decision Tree Classifier.

### Step 8

Evaluate Decision Tree accuracy.

### Step 9

Visualize the Decision Tree.

### Step 10

Train a Random Forest Classifier.

### Step 11

Evaluate Random Forest accuracy.

### Step 12

Extract Feature Importance.

### Step 13

Visualize Feature Importance.

### Step 14

Compare Decision Tree and Random Forest performance.

---

## Project Structure

```
HeartDiseaseProject/
│
├── heart_disease_uci.csv
├── project3.py
└── README.md
```

---

## Output

The program displays:

- Dataset Preview
- Decision Tree Accuracy
- Random Forest Accuracy
- Classification Reports
- Decision Tree Visualization
- Feature Importance Table
- Feature Importance Graph
- Most Important Feature
- Least Important Feature
- Model Comparison

---

## Feature Importance

Feature Importance shows how much each medical feature contributes to predicting heart disease.

Higher importance means the feature has a stronger influence on the model's prediction.

---

## Decision Tree

The Decision Tree is visualized using:

```python
plot_tree()
```

This helps understand how the model makes decisions based on different medical attributes.

---

## Random Forest

Random Forest combines multiple Decision Trees to improve:

- Accuracy
- Stability
- Generalization

It also provides reliable feature importance scores.

---

## Expected Outcome

After completing this project, students will be able to:

- Understand Decision Trees.
- Understand Random Forests.
- Compare tree-based classification models.
- Interpret Feature Importance.
- Apply Machine Learning to healthcare datasets.

---

## Conclusion

This project demonstrates how tree-based machine learning models can be used for heart disease prediction. It compares the performance of Decision Tree and Random Forest classifiers while identifying the most influential medical features through Feature Importance analysis. The project provides practical experience in data preprocessing, model training, evaluation, visualization, and interpretation of results.
