import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales.csv")

# Sales by category
category_sales = df.groupby('Category')['Sales'].sum()

# Create bar chart
category_sales.plot(kind='bar')

# Chart details
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Save chart
plt.savefig("../reports/sales_chart.png")

print("Chart generated successfully!")