
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("data/database/retail.db")

# Read SQL file
with open("sql/retail_analysis.sql", "r") as file:
    sql_content = file.read()

# Separate SQL queries
queries = [
    query.strip()
    for query in sql_content.split(";")
    if query.strip()
]

# Execute queries individually
for number, query in enumerate(queries, start=1):

    print("\n" + "=" * 60)
    print(f"SQL ANALYSIS {number}")
    print("=" * 60)

    result = pd.read_sql_query(query, conn)

    print(result.to_string(index=False))

conn.close()

print("\nALL SQL ANALYSIS COMPLETED!")
