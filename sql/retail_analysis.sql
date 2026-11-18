
-- 1. CATEGORY-WISE SALES AND PROFIT

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;


-- 2. REGION-WISE PERFORMANCE

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Region
ORDER BY Total_Profit DESC;


-- 3. TOP 10 LOSS-MAKING PRODUCTS

SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY "Product Name"
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC
LIMIT 10;


-- 4. DISCOUNT VS PROFIT

SELECT
    Discount,
    COUNT(*) AS Transactions,
    ROUND(AVG(Profit), 2) AS Average_Profit,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Discount
ORDER BY Discount;


-- 5. MONTHLY SALES ANALYSIS

SELECT
    strftime('%Y-%m', "Order Date") AS Order_Month,
    ROUND(SUM(Sales), 2) AS Monthly_Sales
FROM orders
GROUP BY Order_Month
ORDER BY Monthly_Sales DESC
LIMIT 10;


-- 6. OVERALL BUSINESS KPIs

SELECT
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    COUNT(DISTINCT "Order ID") AS Total_Orders,
    COUNT(DISTINCT "Customer ID") AS Total_Customers,
    SUM(Quantity) AS Total_Quantity,
    ROUND(SUM(Profit) * 100.0 / SUM(Sales), 2)
        AS Profit_Margin
FROM orders;
