-- E-Commerce Sales & Customer Analytics
-- PostgreSQL-compatible SQL
-- Import data/sales_data.csv into public.sales_data using your SQL tool's CSV import wizard.
-- Expected columns and types are represented below. If table already exists, skip CREATE TABLE.
CREATE TABLE IF NOT EXISTS sales_data (
    order_id TEXT,
    order_date DATE,
    customer_id TEXT,
    city TEXT,
    region TEXT,
    product TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price_inr NUMERIC(12,2),
    discount_rate NUMERIC(8,4),
    revenue_inr NUMERIC(14,2),
    profit_inr NUMERIC(14,2),
    sales_channel TEXT,
    payment_method TEXT,
    order_status TEXT
);

-- 1. Overall order and customer KPIs
SELECT COUNT(DISTINCT order_id) AS total_orders,
       COUNT(DISTINCT customer_id) AS unique_customers,
       SUM(CASE WHEN LOWER(order_status)='delivered' THEN revenue_inr ELSE 0 END) AS delivered_revenue_inr,
       SUM(CASE WHEN LOWER(order_status)='delivered' THEN profit_inr ELSE 0 END) AS estimated_delivered_profit_inr
FROM sales_data;

-- 2. Order status distribution
SELECT order_status, COUNT(DISTINCT order_id) AS orders,
       ROUND(100.0*COUNT(DISTINCT order_id)/SUM(COUNT(DISTINCT order_id)) OVER (),2) AS share_pct
FROM sales_data GROUP BY order_status ORDER BY orders DESC;

-- 3. Revenue by region
SELECT region, COUNT(DISTINCT order_id) AS delivered_orders,
       SUM(revenue_inr) AS delivered_revenue_inr
FROM sales_data WHERE LOWER(order_status)='delivered'
GROUP BY region ORDER BY delivered_revenue_inr DESC;

-- 4. Category and product performance
SELECT category, product, SUM(quantity) AS units,
       SUM(revenue_inr) AS revenue_inr, SUM(profit_inr) AS estimated_profit_inr
FROM sales_data WHERE LOWER(order_status)='delivered'
GROUP BY category, product ORDER BY revenue_inr DESC;

-- 5. Revenue by sales channel
SELECT sales_channel, COUNT(DISTINCT order_id) AS orders,
       SUM(revenue_inr) AS revenue_inr
FROM sales_data WHERE LOWER(order_status)='delivered'
GROUP BY sales_channel ORDER BY revenue_inr DESC;

-- 6. Monthly revenue trend (CTE)
WITH monthly AS (
  SELECT DATE_TRUNC('month', order_date)::date AS month_start,
         SUM(revenue_inr) AS revenue_inr
  FROM sales_data WHERE LOWER(order_status)='delivered'
  GROUP BY DATE_TRUNC('month', order_date)
)
SELECT month_start, revenue_inr,
       LAG(revenue_inr) OVER (ORDER BY month_start) AS previous_month_revenue
FROM monthly ORDER BY month_start;

-- 7. Top 10 customers (subquery + aggregation)
SELECT customer_id, orders, revenue_inr
FROM (
  SELECT customer_id, COUNT(DISTINCT order_id) AS orders,
         SUM(revenue_inr) AS revenue_inr,
         DENSE_RANK() OVER (ORDER BY SUM(revenue_inr) DESC) AS revenue_rank
  FROM sales_data WHERE LOWER(order_status)='delivered'
  GROUP BY customer_id
) ranked
WHERE revenue_rank <= 10 ORDER BY revenue_rank;

-- 8. Average order value by region
SELECT region, ROUND(SUM(revenue_inr)/NULLIF(COUNT(DISTINCT order_id),0),2) AS avg_order_value_inr
FROM sales_data WHERE LOWER(order_status)='delivered'
GROUP BY region ORDER BY avg_order_value_inr DESC;

-- 9. Payment method mix
SELECT payment_method, COUNT(DISTINCT order_id) AS orders,
       SUM(revenue_inr) AS revenue_inr
FROM sales_data GROUP BY payment_method ORDER BY orders DESC;

-- 10. Data quality checks
SELECT COUNT(*) AS row_count,
       COUNT(*)-COUNT(order_id) AS missing_order_ids,
       COUNT(*)-COUNT(order_date) AS missing_order_dates,
       COUNT(*)-COUNT(customer_id) AS missing_customer_ids
FROM sales_data;
