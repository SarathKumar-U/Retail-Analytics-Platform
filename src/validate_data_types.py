
import pandas as pd

# Load original dataset
df = pd.read_csv(
    "data/raw/Sample - Superstore.csv",
    encoding="latin1"
)

print("1. DATE VALIDATION")

for col in ["Order Date", "Ship Date"]:
    dates = pd.to_datetime(df[col], errors="coerce")

    print(f"\n{col}")
    print("Invalid dates:", dates.isna().sum())
    print("Earliest date:", dates.min())
    print("Latest date:", dates.max())

# Check shipping date consistency
order_dates = pd.to_datetime(df["Order Date"], errors="coerce")
ship_dates = pd.to_datetime(df["Ship Date"], errors="coerce")

print("\n2. SHIPPING DATE VALIDATION")
print(
    "Ship dates before order dates:",
    (ship_dates < order_dates).sum()
)

print("\n3. POSTAL CODE INVESTIGATION")

print("Postal code data type:", df["Postal Code"].dtype)

print("\nFirst 10 postal codes:")
print(df["Postal Code"].head(10).to_list())

print(
    "\nPostal codes with fewer than 5 digits:",
    (df["Postal Code"] < 10000).sum()
)

print("\n4. COUNTRY VALIDATION")
print(df["Country"].value_counts())

print("\nVALIDATION COMPLETED!")
