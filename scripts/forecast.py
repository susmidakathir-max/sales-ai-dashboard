import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

# Load cleaned dataset
df = pd.read_csv("data/cleaned_sales.csv")

# Convert date column
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Group sales by date
monthly_sales = df.groupby('Order Date')['Sales'].sum().reset_index()

# Create index
monthly_sales['Index'] = np.arange(len(monthly_sales))

# Features and target
X = monthly_sales[['Index']]
y = monthly_sales['Sales']

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict future sales
future = pd.DataFrame([[len(monthly_sales)]], columns=['Index'])
prediction = model.predict(future)

print("Predicted Future Sales:", prediction[0])