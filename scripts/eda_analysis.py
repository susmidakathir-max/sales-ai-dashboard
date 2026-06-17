import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sales.csv")

# Basic information
print("\nDataset Info:")
print(df.info())

# First 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# Statistical summary
print("\nSummary Statistics:")
print(df.describe())

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())