
import pandas as pd

# STEP 1: Load cleaned dataset
df = pd.read_csv("data/processed/superstore_cleaned.csv")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("=" * 55)
print("RETAIL ANALYTICS - EXPLORATORY DATA ANALYSIS")
print("=" * 55)

# STEP 2: Overall business KPIs
print("\n1. OVERALL BUSINESS PERFORMANCE")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()

profit_margin = (total_profit / total_sales) * 100

print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Total Quantity Sold:", total_quantity)
print("Profit Margin:", round(profit_margin, 2), "%")

# STEP 3: Category performance
print("\n2. CATEGORY-WISE PERFORMANCE")

category = (
    df.groupby("Category")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum"),
        Quantity=("Quantity", "sum")
    )
    .sort_values("Sales", ascending=False)
)

print(category.round(2))

# STEP 4: Regional performance
print("\n3. REGION-WISE PERFORMANCE")

region = (
    df.groupby("Region")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
    .sort_values("Profit", ascending=False)
)

print(region.round(2))

# STEP 5: Loss-making products
print("\n4. LOSS-MAKING PRODUCTS")

product = (
    df.groupby("Product Name")
    .agg(
        Sales=("Sales", "sum"),
        Profit=("Profit", "sum")
    )
)

loss_products = product[product["Profit"] < 0]
loss_products = loss_products.sort_values("Profit")

print("Number of loss-making products:", len(loss_products))
print("\nTop 10 products with highest losses:")
print(loss_products.head(10).round(2))

# STEP 6: Discount analysis
print("\n5. DISCOUNT VS PROFIT ANALYSIS")

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Average_Profit=("Profit", "mean"),
        Total_Profit=("Profit", "sum"),
        Transactions=("Profit", "count")
    )
    .sort_index()
)

print(discount_analysis.round(2))

# STEP 7: Monthly sales analysis
print("\n6. MONTHLY SALES ANALYSIS")

df["Order Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Order Month")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTop 10 months by sales:")
print(monthly_sales.head(10).round(2))

print("\nEDA COMPLETED SUCCESSFULLY!")
