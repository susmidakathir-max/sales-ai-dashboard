import pandas as pd

# Load cleaned data
df = pd.read_csv("../data/cleaned_sales.csv")

# Calculate important metrics
total_sales = df['Sales'].sum()

top_products = (
    df.groupby('Product Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create summary dataframe
summary = pd.DataFrame({
    'Metric': ['Total Sales'],
    'Value': [total_sales]
})

# Save report
with pd.ExcelWriter("../reports/sales_report.xlsx") as writer:
    summary.to_excel(writer, sheet_name='Summary', index=False)
    top_products.to_excel(writer, sheet_name='Top Products')

print("Automated report generated successfully!")