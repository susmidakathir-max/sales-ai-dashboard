import pandas as pd

# Load dataset
df = pd.read_csv("data/train.csv")

# Remove null values
df = df.dropna()

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)

# Save cleaned file
df.to_csv("data/cleaned_sales.csv", index=False)

print("Data cleaned successfully!")