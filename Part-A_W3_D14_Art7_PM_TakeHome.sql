-- Part A: Concept Application (40%)

-- 1. Running total: cumulative revenue per product category ordered by date.
-- ASSUMING TABLE: sales (date, category, revenue)
SELECT 
    date, 
    category, 
    revenue,
    SUM(revenue) OVER(PARTITION BY category ORDER BY date) AS cumulative_revenue
FROM sales;

-- 2. Top-N: top-3 customers by revenue per city. Use ROW_NUMBER().
-- ASSUMING TABLE: customers (customer_id, city, revenue)
WITH RankedCustomers AS (
    SELECT 
        customer_id, 
        city, 
        revenue,
        ROW_NUMBER() OVER(PARTITION BY city ORDER BY revenue DESC) as rn
    FROM customers
)
SELECT customer_id, city, revenue 
FROM RankedCustomers 
WHERE rn <= 3;

-- 3. MoM growth: month-over-month revenue change % using LAG. Flag months with < −5% change.
-- ASSUMING TABLE: monthly_revenue (month_date, revenue) 
WITH MoM_Calculation AS (
    SELECT 
        month_date, 
        revenue,
        LAG(revenue) OVER(ORDER BY month_date) as prev_revenue
    FROM monthly_revenue
),
Growth_Calculation AS (
    SELECT 
        month_date, 
        revenue, 
        prev_revenue,
        ((revenue - prev_revenue) / prev_revenue) * 100 AS pct_change
    FROM MoM_Calculation
)
SELECT 
    month_date, 
    revenue, 
    pct_change,
    CASE 
        WHEN pct_change < -5.0 THEN 'YES' 
        ELSE 'NO' 
    END as bad_month_flag
FROM Growth_Calculation;

-- 4. Multi-CTE: identify departments where all employees earn above the company average.
-- ASSUMING TABLE: employees (emp_id, dept_id, salary) 
WITH CompanyAverage AS (
    SELECT AVG(salary) AS avg_sal 
    FROM employees
),
EmployeeStatus AS (
    SELECT 
        e.dept_id,
        CASE WHEN e.salary > c.avg_sal THEN 1 ELSE 0 END as is_above_avg
    FROM employees e
    CROSS JOIN CompanyAverage c
)
SELECT dept_id
FROM EmployeeStatus
GROUP BY dept_id
HAVING MIN(is_above_avg) = 1;

-- 5. Correlated subquery: find the 2nd highest salary per department WITHOUT window functions.
-- ASSUMING TABLE: employees (emp_id, dept_id, salary)
SELECT e1.dept_id, MAX(e1.salary) AS second_highest_salary
FROM employees e1
WHERE e1.salary < (
    SELECT MAX(e2.salary) 
    FROM employees e2 
    WHERE e1.dept_id = e2.dept_id
)
GROUP BY e1.dept_id;
