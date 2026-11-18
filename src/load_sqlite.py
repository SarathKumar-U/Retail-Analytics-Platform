import pandas as pd
import sqlite3
import os

# Load cleaned dataset
df = pd.read_csv("data/processed/superstore_cleaned.csv")

# Create database folder
os.makedirs("data/database", exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect("data/database/retail.db")

# Load data into SQL table
df.to_sql("orders", conn, if_exists="replace", index=False)

# Verify insertion
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM orders")
print("Total records in SQL:", cursor.fetchone()[0])

cursor.execute("SELECT COUNT(DISTINCT \"Order ID\") FROM orders")
print("Unique orders:", cursor.fetchone()[0])

conn.close()

print("\nSQL DATABASE CREATED SUCCESSFULLY!")
