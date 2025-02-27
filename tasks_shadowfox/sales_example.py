import pandas as pd

# Load dataset
file_path = "C:\\Users\\kasan\\OneDrive\\Desktop\\task_2_shadowfox\\sales_data.csv"
df = pd.read_csv(file_path)

# Clean column names
df.columns = df.columns.str.strip()

# Check actual column names
print("Columns in dataset:", df.columns)

# Ensure correct column names are used
if "Net Sales" in df.columns and "COGS" in df.columns:
    df["Profit_Margin"] = (df["Net Sales"] - df["COGS"]) / df["Net Sales"] * 100
    print(df.head())  # Display first few rows
else:
    print("Error: Column names do not match expected values. Please check dataset.")


df.to_csv("C:\\Users\\kasan\\OneDrive\\Desktop\\task_2_shadowfox\\updated_sales_data.csv", index=False)
