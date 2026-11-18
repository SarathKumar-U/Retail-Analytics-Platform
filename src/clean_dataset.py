
import pandas as pd
import os

# STEP 1: Load original dataset
df = pd.read_csv(
    "data/raw/Sample - Superstore.csv",
    encoding="latin1"
)

original_rows = len(df)

print("STEP 1: ORIGINAL DATASET")
print("Total records:", original_rows)

# STEP 2: Convert date columns
df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    format="%m/%d/%Y",
    errors="raise"
)

df["Ship Date"] = pd.to_datetime(
    df["Ship Date"],
    format="%m/%d/%Y",
    errors="raise"
)

print("\nSTEP 2: DATE CONVERSION COMPLETED")

# STEP 3: Correct postal code representation
df["Postal Code"] = (
    df["Postal Code"]
    .astype("Int64")
    .astype("string")
    .str.zfill(5)
)

print("\nSTEP 3: POSTAL CODE CORRECTION")
print("Postal code data type:", df["Postal Code"].dtype)
print("Postal code lengths:")
print(df["Postal Code"].str.len().value_counts())

# STEP 4: Verify dataset integrity
print("\nSTEP 4: DATASET VERIFICATION")

print("Original records:", original_rows)
print("Cleaned records:", len(df))
print("Missing values:", df.isnull().sum().sum())
print("Duplicate rows:", df.duplicated().sum())
print(
    "Invalid postal code lengths:",
    (~df["Postal Code"].str.len().eq(5)).sum()
)

# STEP 5: Save cleaned dataset separately
os.makedirs("data/processed", exist_ok=True)

output_path = "data/processed/superstore_cleaned.csv"

df.to_csv(output_path, index=False)

print("\nSTEP 5: DATASET SAVED")
print("Location:", output_path)

print("\nDATA CLEANING COMPLETED SUCCESSFULLY!")
