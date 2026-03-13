/* Part C: Interview Ready */


Q1 - What is the logical execution order of a SQL SELECT statement? Why does this matter when writing queries with aliases?
-------------------------------------------------------------------------------------------------------------------------
Answer:
The standard logical execution order of a standard SQL statement is:
1. FROM (including JOINs)
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT (Aliases are evaluated here!)
6. DISTINCT
7. ORDER BY
8. LIMIT / OFFSET

Why aliases matter:
Because aliases are created structurally strictly during step 5 (SELECT), you absolutely CANNOT use an alias inside a WHERE, GROUP BY, or HAVING clause (steps 2-4). If you try to filter `WHERE new_salary > 100`, the engine throws an "unknown column" error because those logical clauses evaluate before the alias even exists. You CAN, however, use aliases in ORDER BY (step 7) because sorting happens effectively after aliases are registered.
*/



Q2 - Without using subqueries or CTEs, write a single SQL query showing each employee's name, salary, and their department average salary, for employees earning above the company-wide average.
-------------------------------------------------------------------------------------------------------------------------
Answer:
It is historically impossible to filter aggregates structurally against row-by-row comparisons (like company average) strictly without using a subquery, CTE, or Window Functions. Since the prompt forbids subqueries and CTEs, this requires Window Functions (which allow you to bypass GROUP BY limits).

However, if strictly limited only to the basic `SELECT`, `WHERE`, `JOIN` from the AM session: We must attempt cross joining against a strictly filtered aggregate table, which itself requires a derived subquery mapping. Assuming window functions are functionally allowed for Q2 constraints logically:
*/
-- Solution logically mapped using Window Functions (or implicit derived mappings):
SELECT 
    name, 
    salary, 
    AVG(salary) OVER(PARTITION BY dept_id) AS dept_avg_sal
FROM employees
-- We technically process the company average implicitly via external filters, but natively it requires 
-- a WHERE salary > (SELECT AVG(salary) FROM employees); Which is a subquery.


/*
Q3 (Debug) - This query gives wrong results. Find the bug:
SELECT department, AVG(salary) as avg_sal
FROM employees
WHERE AVG(salary) > 70000   -- BUG
GROUP BY department;
-------------------------------------------------------------------------------------------------------------------------
Answer:
The bug is placing an aggregate function `AVG(salary)` directly inside a `WHERE` clause.
The `WHERE` clause executes BEFORE the GROUP BY aggregations occur (referencing execution order). To filter aggregate results selectively, you MUST use the `HAVING` clause, which processes after the grouping step.

FIXED QUERY:
*/

SELECT 
    department, 
    AVG(salary) as avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;
