
import pandas as pd

# Load the Excel file
file_path = "sales_data.xlsx"  # Path to your file
df = pd.read_excel(file_path)

# Calculate total and average sales
total_sales = df['Sales'].sum()
average_sales = df['Sales'].mean()

# Filter high-performing regions (sales > 5000)
high_performers = df[df['Sales'] > 5000]

# Create a summary DataFrame
summary = pd.DataFrame({
    "Metric": ["Total Sales", "Average Sales"],
    "Value": [total_sales, average_sales]
})

# Save the results
with pd.ExcelWriter("sales_summary.xlsx") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    high_performers.to_excel(writer, sheet_name="High Performers", index=False)

print("Sales summary and high performers saved to sales_summary.xlsx!")
