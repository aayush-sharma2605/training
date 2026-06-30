# Customer Data Preprocessing Pipeline

## Project Description

This project demonstrates the complete data preprocessing workflow using Python, Pandas, and Scikit-learn. The program loads customer data from a CSV file, handles missing values, creates new features, scales numerical data, encodes categorical data, and saves the cleaned dataset for further analysis or machine learning.

---

## Objectives

- Load a CSV dataset using Pandas.
- Identify and handle missing values.
- Create new features using feature engineering.
- Scale numerical features using StandardScaler.
- Encode categorical features using LabelEncoder.
- Save the cleaned dataset into a new CSV file.

---

## Technologies Used

- Python 3.x
- Pandas
- Scikit-learn

---

## Dataset

Dataset Used:

**Mall_Customers.csv**

Columns:

- CustomerID
- Genre
- Age
- Annual Income (k$)
- Spending Score (1-100)

---

## Features Implemented

### 1. Load Dataset

Reads the CSV file into a Pandas DataFrame.

```python
pd.read_csv("Mall_Customers.csv")
```

---

### 2. Missing Value Handling

- Checks for missing values.
- Replaces missing numerical values using the column mean.
- Replaces missing categorical values using the mode.

---

### 3. Feature Engineering

Created two new features:

- **Age_Group**
  - Teen
  - Adult
  - Middle Age
  - Senior

- **Income_Level**
  - Low
  - Medium
  - High

---

### 4. Feature Scaling

Scaled numerical columns:

- Age
- Annual Income (k$)
- Spending Score (1-100)

using **StandardScaler**.

---

### 5. Label Encoding

Converted the **Genre** column into numerical values using **LabelEncoder**.

Example:

```
Female → 0
Male → 1
```

---

### 6. Save Cleaned Dataset

The processed dataset is saved as:

```
Cleaned_Mall_Customers.csv
```

---

## Required Libraries

Install the required libraries before running the program.

```bash
pip install pandas
pip install scikit-learn
```

or

```bash
pip install pandas scikit-learn
```

---

## How to Run

Open the terminal in the project folder and run:

```bash
python Project3.py
```

---

## Output Files

- Cleaned_Mall_Customers.csv

---

## Learning Outcomes

After completing this project, you will understand:

- Reading CSV files using Pandas
- Handling missing values
- Feature Engineering
- Feature Scaling
- Label Encoding
- Saving processed datasets
- Data preprocessing techniques used before machine learning

---

## Author

**Name:** Aayush Sharma

**Course:** B.Tech Artificial Intelligence & Machine Learning

**Project:** Customer Data Preprocessing Pipeline
