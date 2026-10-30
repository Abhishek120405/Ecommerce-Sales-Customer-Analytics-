-- SQLite-compatible companion to ecommerce_sales_analysis.sql
-- Import data/sales_data.csv into a table named sales_data before running.
-- These queries are executable in SQLite; the PostgreSQL file remains the primary SQL portfolio version.

-- 1. Overall order and customer KPIs
SELECT COUNT(DISTINCT Order_ID) AS total_orders,
       COUNT(DISTINCT Customer_ID) AS unique_customers,
       SUM(CASE WHEN LOWER(Order_Status)='delivered' THEN Revenue_INR ELSE 0 END) AS delivered_revenue_inr,
       SUM(CASE WHEN LOWER(Order_Status)='delivered' THEN Profit_INR ELSE 0 END) AS estimated_delivered_profit_inr
FROM sales_data;

-- 2. Order status distribution
SELECT Order_Status, COUNT(DISTINCT Order_ID) AS orders,
       ROUND(100.0*COUNT(DISTINCT Order_ID)/SUM(COUNT(DISTINCT Order_ID)) OVER (),2) AS share_pct
FROM sales_data GROUP BY Order_Status ORDER BY orders DESC;

-- 3. Revenue by region
SELECT Region, COUNT(DISTINCT Order_ID) AS delivered_orders,
       SUM(Revenue_INR) AS delivered_revenue_inr
FROM sales_data WHERE LOWER(Order_Status)='delivered'
GROUP BY Region ORDER BY delivered_revenue_inr DESC;

-- 4. Category and product performance
SELECT Category, Product, SUM(Quantity) AS units,
       SUM(Revenue_INR) AS revenue_inr, SUM(Profit_INR) AS estimated_profit_inr
FROM sales_data WHERE LOWER(Order_Status)='delivered'
GROUP BY Category, Product ORDER BY revenue_inr DESC;

-- 5. Revenue by sales channel
SELECT Sales_Channel, COUNT(DISTINCT Order_ID) AS orders,
       SUM(Revenue_INR) AS revenue_inr
FROM sales_data WHERE LOWER(Order_Status)='delivered'
GROUP BY Sales_Channel ORDER BY revenue_inr DESC;

-- 6. Monthly revenue trend
WITH monthly AS (
  SELECT date(Order_Date, 'start of month') AS month_start,
         SUM(Revenue_INR) AS revenue_inr
  FROM sales_data WHERE LOWER(Order_Status)='delivered'
  GROUP BY date(Order_Date, 'start of month')
)
SELECT month_start, revenue_inr,
       LAG(revenue_inr) OVER (ORDER BY month_start) AS previous_month_revenue
FROM monthly ORDER BY month_start;

-- 7. Top 10 customers
SELECT Customer_ID, orders, revenue_inr
FROM (
  SELECT Customer_ID, COUNT(DISTINCT Order_ID) AS orders,
         SUM(Revenue_INR) AS revenue_inr,
         DENSE_RANK() OVER (ORDER BY SUM(Revenue_INR) DESC) AS revenue_rank
  FROM sales_data WHERE LOWER(Order_Status)='delivered'
  GROUP BY Customer_ID
) ranked
WHERE revenue_rank <= 10 ORDER BY revenue_rank;

-- 8. Average order value by region
SELECT Region, ROUND(SUM(Revenue_INR)/NULLIF(COUNT(DISTINCT Order_ID),0),2) AS avg_order_value_inr
FROM sales_data WHERE LOWER(Order_Status)='delivered'
GROUP BY Region ORDER BY avg_order_value_inr DESC;

-- 9. Payment method mix
SELECT Payment_Method, COUNT(DISTINCT Order_ID) AS orders,
       SUM(Revenue_INR) AS revenue_inr
FROM sales_data GROUP BY Payment_Method ORDER BY orders DESC;

-- 10. Data quality checks
SELECT COUNT(*) AS row_count,
       COUNT(*)-COUNT(Order_ID) AS missing_order_ids,
       COUNT(*)-COUNT(Order_Date) AS missing_order_dates,
       COUNT(*)-COUNT(Customer_ID) AS missing_customer_ids
FROM sales_data;
