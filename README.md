# E-Commerce Data Validation Script

## Overview
This Python script validates an e-commerce dataset by identifying inconsistencies and potential errors in the data. It systematically checks for:
- **Missing values:** Ensures all required fields are populated.
- **Future orders:** Flags records where `Future_OrderDate` is set to `True`.
- **Unusual quantity values:** Detects anomalies where `Quantity` is either negative or exceeds a reasonable limit (e.g., 100).
- **Total amount mismatches:** Verifies if `TotalAmount` correctly matches the expected value (`Quantity * Price`).

The script generates a **log file** summarizing all detected issues, which is stored on the user's desktop in Excel format.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Pandas (`pip install pandas`)
- OpenPyXL (`pip install openpyxl`)

## Setup
1. Place the dataset (`ecommerce-dataset-final.csv`) in a location accessible by the script.
2. Update the file path inside the script to match the dataset location:
   ```python
   file_path = r"C:\Users\mhash\OneDrive\Desktop\ecommerce-dataset-final.csv"
