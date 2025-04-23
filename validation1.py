import pandas as pd
from datetime import datetime

# Load dataset
file_path = r"C:\Users\mhash\OneDrive\Desktop\ecommerce-dataset-final.csv"
df = pd.read_csv(file_path)

# Initialize log dictionary
log_data = {
    "Excel_Row_Number": [],  
    "Issue": [],
    "Details": []
}

# Identify missing values
missing_values = df[df.isnull().any(axis=1)]
for index, row in missing_values.iterrows():
    log_data["Excel_Row_Number"].append(index + 2)  # +2 to match Excel row 
    log_data["Issue"].append("Missing Values")
    log_data["Details"].append(f"Columns with missing values: {row.isnull().sum()}")

# Log future orders only if 'Future_OrderDate' is True and the column exists
if 'Future_OrderDate' in df.columns: 
    for index, row in df.iterrows():
        try:  # Handle potential type errors in 'Future_OrderDate' column
            if row['Future_OrderDate']:  # Check if 'Future_OrderDate' is True
                log_data["Excel_Row_Number"].append(index + 2)  # Adjust for Excel row numbering
                log_data["Issue"].append("Future_OrderDate")  
                # Update Details message to mention 'Future_OrderDate' field
                log_data["Details"].append("• Flag future-dated entries in the `Future_OrderDate` field: True") 
        except (TypeError, ValueError):
            print(f"Warning: Invalid value in 'Future_OrderDate' column at row {index + 2}")
                
# Detect unusual 'Quantity' values
unusual_quantity = df[(df["Quantity"] < 0) | (df["Quantity"] > 100)]
for index, row in unusual_quantity.iterrows():
    log_data["Excel_Row_Number"].append(index + 2)
    log_data["Issue"].append("Quantity Outlier")
    log_data["Details"].append(f"Quantity: {row['Quantity']}")

# Validate 'TotalAmount'
df["ExpectedTotal"] = df["Quantity"] * df["Price"]
invalid_total = df[df["TotalAmount"].round(2) != df["ExpectedTotal"].round(2)]
for index, row in invalid_total.iterrows():
    log_data["Excel_Row_Number"].append(index + 2)
    log_data["Issue"].append("TotalAmount Mismatch")
    log_data["Details"].append(f"Expected: {row['ExpectedTotal']}, Found: {row['TotalAmount']}")

# Save log to Excel
log_df = pd.DataFrame(log_data)
log_file_path = r"C:\Users\mhash\OneDrive\Desktop\data_validation_log.xlsx"
log_df.to_excel(log_file_path, index=False, engine="openpyxl")

print(f"Validation complete. Log saved to {log_file_path}.")
