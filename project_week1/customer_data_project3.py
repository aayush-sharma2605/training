import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

 
# Load Dataset
 

df = pd.read_csv("Mall_Customers.csv")

print("========== Original Dataset ==========\n")
print(df.head())

 
# Check Missing Values
 

print("\n========== Missing Values ==========\n")
print(df.isnull().sum())

# Fill missing numerical values with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Annual Income (k$)"] = df["Annual Income (k$)"].fillna(df["Annual Income (k$)"].mean())
df["Spending Score (1-100)"] = df["Spending Score (1-100)"].fillna(df["Spending Score (1-100)"].mean())

# Fill missing categorical values with mode
df["Genre"] = df["Genre"].fillna(df["Genre"].mode()[0])

 
# Feature Engineering
 

# Age Group

def age_group(age):
    if age < 20:
        return "Teen"
    elif age < 40:
        return "Adult"
    elif age < 60:
        return "Middle Age"
    else:
        return "Senior"

df["Age_Group"] = df["Age"].apply(age_group)

# Income Level

def income_level(income):
    if income < 40:
        return "Low"
    elif income < 70:
        return "Medium"
    else:
        return "High"

df["Income_Level"] = df["Annual Income (k$)"].apply(income_level)

print("\n========== After Feature Engineering ==========\n")
print(df.head())

 
# Feature Scaling
 

scaler = StandardScaler()

numerical_columns = [
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

df[numerical_columns] = scaler.fit_transform(df[numerical_columns])

print("\n========== After Scaling ==========\n")
print(df.head())

 
# Label Encoding
 

label_encoder = LabelEncoder()

df["Genre"] = label_encoder.fit_transform(df["Genre"])

print("\n========== After Label Encoding ==========\n")
print(df.head())

 
# Save Cleaned Dataset
 

df.to_csv("Cleaned_Mall_Customers.csv", index=False)

print("\nCleaned dataset saved as Cleaned_Mall_Customers.csv")