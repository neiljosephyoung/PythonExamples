
import pandas as pd

# Load the Excel file
file_path = "inventory.xlsx"
df = pd.read_excel(file_path)

# Identify items with stock < 50
low_stock = df[df['Stock'] < 50]

# Save to a new sheet
with pd.ExcelWriter("low_stock_alerts.xlsx") as writer:
    df.to_excel(writer, sheet_name="Full Inventory", index=False)
    low_stock.to_excel(writer, sheet_name="Low Stock Alerts", index=False)

print("Low stock alerts saved to low_stock_alerts.xlsx!")
