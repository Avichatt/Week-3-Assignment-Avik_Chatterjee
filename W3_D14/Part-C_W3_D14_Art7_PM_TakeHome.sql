-- Part C: Interview Ready (20%)

/*
-------------------------------------------------------------------------------------------------------------------
Q1 - Explain the difference between RANK() and DENSE_RANK(). When does the difference matter in a business context?
-------------------------------------------------------------------------------------------------------------------
Answer:
- RANK() assigns sequential rankings but LEAVES GAPS when ties occur. 
  (For example: If two people tie for 1st place, the ranks will be 1, 1, 3... rank 2 is completely skipped).
- DENSE_RANK() structurally ignores gaps and issues strictly consecutive identifiers regardless of ties.
  (For example: If two people tie for 1st, ranks will be 1, 1, 2... rank 2 is preserved immediately afterward).

Business Context Difference:
If a company is distributing bonuses to the literal "Top 3 highest salespeople", DENSE_RANK() ensures that the entity placing 3rd dimensionally still gets rewarded (ranks 1, 1, 2, 3). If you use strictly normal RANK(), the sequence would be 1, 1, 3, 4, meaning the 4th person (who was structurally #3 in volume) is cut out entirely by a "Top 3" clause.
*/


/*
-------------------------------------------------------------------------------------------------------------------
Q2 (Coding) - Given transactions(user_id, transaction_date, amount), write a query that finds users who 
made a purchase in 3 or more consecutive months. Use window functions.
-------------------------------------------------------------------------------------------------------------------
*/

WITH MonthlyTransactions AS (
    -- First, reduce multiple purchases within the exact same month down to a single unique marker per month per user.
    -- (DATE_FORMAT converts date to string mapping 'YYYY-MM-01' so standard date functions work consistently)
    SELECT DISTINCT 
        user_id, 
        DATE_FORMAT(transaction_date, '%Y-%m-01') AS purchase_month
    FROM transactions
),
Lags AS (
    -- Apply LAG functions sorting by date to fetch previous months sequentially. 
    -- We want to peek back 1 month, and also 2 months simultaneously.
    SELECT 
        user_id, 
        purchase_month, 
        LAG(purchase_month, 1) OVER(PARTITION BY user_id ORDER BY purchase_month) as prev_1_month,
        LAG(purchase_month, 2) OVER(PARTITION BY user_id ORDER BY purchase_month) as prev_2_month
    FROM MonthlyTransactions
)
-- Filter users whose last two historic purchases strictly overlap math boundaries indicating consecutive unbroken months.
SELECT DISTINCT user_id
FROM Lags
WHERE prev_1_month = DATE_SUB(purchase_month, INTERVAL 1 MONTH)
  AND prev_2_month = DATE_SUB(purchase_month, INTERVAL 2 MONTH);


/*
-------------------------------------------------------------------------------------------------------------------
Q3 (Optimise) - Rewrite this correlated subquery as a window function:
SELECT name, salary FROM employees e1
WHERE salary > (SELECT AVG(salary) FROM employees e2 WHERE e2.department = e1.department);
-------------------------------------------------------------------------------------------------------------------
*/

-- Rewritten Optimized Code using Window Functions (MySQL 8.0+):
WITH DeptAverageCTE AS (
    SELECT 
        name, 
        salary, 
        AVG(salary) OVER(PARTITION BY department) as avg_dept_sal
    FROM employees
)
SELECT name, salary
FROM DeptAverageCTE
WHERE salary > avg_dept_sal;

/*
Optimization Reason / Understanding:
The original correlated subquery forces the SQL engine into an O(N^2) time complexity bottleneck. It executed the aggregate average sub-calculation implicitly row-by-row for every single employee independently. 

By rewriting it inside a Window Function `AVG() OVER()`, the engine computes the departmental average logically in a single deterministic pass across the dataset reducing time scaling massively to O(N) or O(N log N) effectively solving performance constraints.
*/
