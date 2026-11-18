
# ==========================================
# PROJECT: RETAIL ANALYTICS PLATFORM
# TASK: INITIAL DATASET INSPECTION
# ==========================================

import pandas as pd

# STEP 1: Load the dataset
file_path = "data/raw/Sample - Superstore.csv"

df = pd.read_csv(
    file_path,
    encoding="latin-1"
)

# STEP 2: Display first five records
print("\n--- FIRST FIVE RECORDS ---")
print(df.head())

# STEP 3: Display last five records
print("\n--- LAST FIVE RECORDS ---")
print(df.tail())

# STEP 4: Display dataset dimensions
print("\n--- DATASET DIMENSIONS ---")
print("Rows and columns:", df.shape)

# STEP 5: Display column names
print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

# STEP 6: Display data types
print("\n--- DATA TYPES ---")
print(df.dtypes)

# STEP 7: Display dataset information
print("\n--- DATASET INFORMATION ---")
df.info()

# STEP 8: Display statistical summary
print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

print("\nDATASET INSPECTION COMPLETED!")
