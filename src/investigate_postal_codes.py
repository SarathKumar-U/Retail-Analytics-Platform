
import pandas as pd

# Load original dataset
df = pd.read_csv(
    "data/raw/Sample - Superstore.csv",
    encoding="latin1"
)

# Filter postal codes containing fewer than 5 digits
low_codes = df[df["Postal Code"] < 10000]

print("1. TOTAL AFFECTED RECORDS")
print(len(low_codes))

print("\n2. UNIQUE AFFECTED POSTAL CODES")
print(sorted(low_codes["Postal Code"].unique()))

print("\n3. POSTAL CODE FREQUENCY")
print(low_codes["Postal Code"].value_counts())

print("\n4. POSTAL CODE WITH CITY AND STATE")
print(
    low_codes[
        ["Postal Code", "City", "State"]
    ].drop_duplicates().sort_values("Postal Code").to_string(index=False)
)

print("\n5. POSTAL CODE DIGIT LENGTH DISTRIBUTION")
print(
    df["Postal Code"]
    .astype(str)
    .str.len()
    .value_counts()
    .sort_index()
)

print("\nPOSTAL CODE INVESTIGATION COMPLETED!")
