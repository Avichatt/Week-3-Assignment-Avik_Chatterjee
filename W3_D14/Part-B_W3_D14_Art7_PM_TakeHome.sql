-- Part B: Stretch Problem (30%)
-- Research RECURSIVE CTEs. 
-- Write a query that generates a number series from 1 to 100 using a recursive CTE (no hard-coded values). 
-- Then use it to fill in missing dates in a sparse time series (dates with no orders appear with revenue=0).

-- Step 1: Generate a mathematical 1 to 100 series via a recursive CTE natively in MySQL 8.0+
WITH RECURSIVE NumberSeries AS (
    SELECT 1 AS num
    UNION ALL
    SELECT num + 1 
    FROM NumberSeries 
    WHERE num < 100
)
SELECT num FROM NumberSeries;

-- Step 2: Utilize the Recursive CTE logic to dynamically generate Dates and Left Join our missing sparse records.
-- ASSUMING TABLE: orders (order_date, revenue)
WITH RECURSIVE DateSeries AS (
    -- Anchor Date: The earliest date in our records (or an arbitrary start timeline)
    SELECT (SELECT MIN(order_date) FROM orders) AS dt
    
    UNION ALL
    
    -- Recursive Step: Add 1 day recursively utilizing MySQL DATE_ADD function
    SELECT DATE_ADD(dt, INTERVAL 1 DAY) 
    FROM DateSeries 
    WHERE dt < (SELECT MAX(order_date) FROM orders)
)
SELECT 
    d.dt AS full_date_series, 
    COALESCE(o.revenue, 0) AS daily_revenue
FROM DateSeries d
LEFT JOIN orders o ON d.dt = o.order_date
ORDER BY d.dt ASC;
