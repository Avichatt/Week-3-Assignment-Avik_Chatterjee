/* Part D: AI-Augmented Task */

/*
PROMPT USED:
"Generate 5 medium-difficulty SQL interview questions for a data engineer role, with answers. Include one about JOINs, one about NULL handling, and one about performance."

-----------------------------------------------------------------------------------
AI OUTPUT (Evaluated Questions & Queries):

Q1: (NULL Handling) Write a query to find all employees who do not belong to a department, ensuring you use a safe NULL fallback returning 'N/A' for their department name output.
A1:
SELECT e.name, COALESCE(d.dept_name, 'N/A') as allocated_dept
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
WHERE e.dept_id IS NULL;

Q2: (Aggregates) Find the second highest salary strictly out of all employees without using a Window Function.
A2:
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

Q3: (JOINs & Conditional Logic) Display the employee name alongside their project name using a 3-table join, but ONLY for projects started before January 1st, 2025. Give the project a fallback alias "No Active Project" if none exists.
A3:
SELECT e.name, COALESCE(p.project_name, 'No Active Project') as project
FROM employees e
LEFT JOIN projects p ON e.emp_id = p.lead_emp_id AND p.start_date < '2025-01-01';

Q4: (Performance / Indexes) You execute an INNER JOIN on a massive millions-row table filtering by `employee_id`, and explain shows a "Sequential Scan". How do you optimize this query and verify indexing worked?
A4: (Conceptual + Syntax)
-- You establish an index to alter plan from sequential to B-Tree Index Scan:
CREATE INDEX idx_emp_id ON employees(emp_id);
-- Verify by applying EXPLAIN QUERY PLAN recursively checking for 'SEARCH USING INDEX' instead of 'SCAN'.

Q5: (Aggregates + Having) List the department IDs that possess strictly more than 10 employees where the average salary across the department exceeds 100,000.
A5:
SELECT dept_id, COUNT(*) as emp_count, AVG(salary) as avg_salary
FROM employees
GROUP BY dept_id
HAVING COUNT(*) > 10 AND AVG(salary) > 100000;


-----------------------------------------------------------------------------------
CRITICAL EVALUATION (200 Words):
Are the questions genuinely medium-difficulty?
Yes. Q2 forces candidates to understand subqueries without defaulting entirely to modern `DENSE_RANK() OVER()` windows. Q3 intelligently checks the difference between placing conditional logic natively within a `LEFT JOIN` `ON` statement versus a standard `WHERE` clause (which incorrectly converts left joins into inner joins if evaluated aggressively on right-tables). 

Are answers complete? 
The answers supply working operational code capable of directly translating perfectly across PostgreSQL and SQLite logic parameters cleanly. However, I corrected the AI’s initial query for Q3. Originally, the AI placed the `p.start_date < '2025-01-01'` directly inside a `WHERE` block after the `LEFT JOIN`. Doing that natively discards all employees lacking a valid match—ruining the 'fallback' requirement structurally. I actively refactored the query to encapsulate the filter strictly within the `ON` clause bindings to effectively protect the `LEFT JOIN` fallback preservation safely.
*/
