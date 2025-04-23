# E-Commerce Data Validation Script

## Overview
This Python script validates an e-commerce dataset by identifying inconsistencies and potential errors in the data. It systematically checks for:
- **Missing values:** Ensures all required fields are populated.
- **Future orders:** Flags records where `Future_OrderDate` is set to `True`.
- **Unusual quantity values:** Detects anomalies where `Quantity` is either negative or exceeds a reasonable limit (e.g., 100).
- **Total amount mismatches:** Verifies if `TotalAmount` correctly matches the expected value (`Quantity * Price`).

The script generates a **log file** summarizing all detected issues, which is stored on the user's desktop in Excel format.

## How to Run the Script

Download the validation1.py Python script.

Download the Excel dataset file.

Set the File Path
In the validation1.py script, locate the file_path variable and update it with the full path to your dataset file on your machine.

Open the terminal or command prompt and navigate to the folder containing validation1.py, then run:

python validation1.py

Check the Output
After running the script, a log file named data_validation_log.xlsx will be created in the same directory (or a specified output path). This file contains all detected validation issues.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Pandas (`pip install pandas`)
- OpenPyXL (`pip install openpyxl`)
