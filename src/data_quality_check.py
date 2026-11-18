
import pandas as pd

# Load original dataset
df = pd.read_csv(
    "data/raw/Sample - Superstore.csv",
    encoding="latin-1"
)

print("\n1. MISSING VALUES")
print(df.isnull().sum())

print("\n2. TOTAL MISSING VALUES")
print(df.isnull().sum().sum())

print("\n3. DUPLICATE ROWS")
print(df.duplicated().sum())

print("\n4. DUPLICATE ROW IDs")
print(df["Row ID"].duplicated().sum())

print("\n5. DATA TYPES")
print(df.dtypes)

print("\n6. UNIQUE VALUES IN CATEGORY")
print(df["Category"].unique())

print("\n7. UNIQUE VALUES IN REGION")
print(df["Region"].unique())

print("\n8. NUMERICAL SUMMARY")
print(df.describe())

print("\nDATA QUALITY CHECK COMPLETED!")
