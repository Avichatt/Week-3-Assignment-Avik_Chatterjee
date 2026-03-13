-- Part D: AI-Augmented Task (10%)

/* 
-------------------------------------------------------------------------------------------------------------------
1. PROMPT SUBMITTED TO AI: 
"Give me 3 MySQL interview questions at senior data engineer level involving window functions or CTEs. Include the 
expected answer and a common mistake candidates make."
-------------------------------------------------------------------------------------------------------------------

AI OUTPUT:

Q1: (Window Functions) Find the top 2 highest paid employees in each department. If there is a tie, include all tied employees.
Answer: 
WITH RankedEmployees AS (
    SELECT name, salary, dept_id,
           DENSE_RANK() OVER(PARTITION BY dept_id ORDER BY salary DESC) as rnk
    FROM employees
)
SELECT name, salary, dept_id FROM RankedEmployees WHERE rnk <= 2;
Common Mistake: Candidates often fall back to ROW_NUMBER(), which strictly limits row counts and arbitrarily cuts off functional ties, implicitly ignoring the 'include all tied employees' evaluation requirement constraint.

Q2: (Aggregation / CTEs) Find departments containing a higher total aggregated salary grouping than the total company-wide average departmental salary threshold.
Answer: 
WITH DeptSums AS (
    SELECT dept_id, SUM(salary) as total_sal FROM employees GROUP BY dept_id
),
CompanyAvg AS (
    SELECT AVG(total_sal) as avg_dept_sal FROM DeptSums
)
SELECT d.dept_id FROM DeptSums d
CROSS JOIN CompanyAvg c
WHERE d.total_sal > c.avg_dept_sal;
Common Mistake: Nested aggregate logic attempts like AVG(SUM(salary)) heavily cause cascading SQL Syntax exceptions because standard engines logically block nested aggregate mappings without wrapping Subquery/CTE definitions.

Q3: (CTEs / Gaps & Islands) Calculate total continuous consecutive daily login streaks returning start/end dates for each user.
Answer: 
WITH CTE_Groupings AS (
    SELECT user_id, login_date,
           DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY login_date) DAY) as island_date
    FROM daily_logins
)
SELECT user_id, MIN(login_date) as streak_start, MAX(login_date) as streak_end, COUNT(*) as streak_days
FROM CTE_Groupings
GROUP BY user_id, island_date;
Common Mistake: Senior Data Engineers mistakenly rely upon incredibly complex Recursive CTEs assuming deep looping requirements blindly; recursively processing deep logs causes horrific infinite looping or heavy computational time bottlenecks instead of using standard partition mathematics to derive contiguous 'Islands'.


-------------------------------------------------------------------------------------------------------------------
2/3. CRITICAL EVALUATION (Self-Assessment & Verification):

Are the common mistakes accurate? 
Yes, significantly so. I've personally seen the DENSE_RANK vs ROW_NUMBER distinction structurally trip up analysts who don't prioritize boundary condition overlaps natively in their syntax. Similarly, attempting recursion to solve Continuous Logs (Gaps and Islands problem) frequently takes hundreds of lines explicitly, when mathematically subtracting row indices logically bounds contiguous sequences inside constant variables optimally via DATE_SUB dynamically.

Did I make any myself? 
During my structural answer for "3 consecutive months" in Part C, I initially attempted to process the math utilizing basic `SELECT (purchase_month - prev_month) = 1` which is a fundamental common mistake manipulating string/dates. Converting months algebraically explicitly fails upon December->January (12 to 1) rollovers. To securely solve it natively I deployed explicit `DATE_SUB(month, INTERVAL 1 MONTH)` standard syntax which properly enforces rollover bounds gracefully on dates.
-------------------------------------------------------------------------------------------------------------------
*/
