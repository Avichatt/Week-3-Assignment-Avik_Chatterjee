-- Part B: Stretch Problem

-- 1. Create a logical projects table
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    lead_emp_id INT,
    budget DECIMAL(10,2),
    start_date DATE,
    end_date DATE
);

-- Note: departments and employees tables are assumed to exist based on typical DDL schemas 
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50),
    dept_budget DECIMAL(12,2)
);

CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    name VARCHAR(50),
    dept_id INT,
    salary DECIMAL(10,2),
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
);

-- Insert 5 Sample rows into projects
INSERT INTO projects (project_id, project_name, lead_emp_id, budget, start_date, end_date) 
VALUES 
(1, 'Alpha Modernization', 1, 150000.00, '2024-01-01', '2024-12-31'),
(2, 'Beta Expansion', 2, 250000.00, '2024-03-01', '2024-08-31'),
(3, 'Gamma Infrastructure', 1, 50000.00, '2024-06-01', '2024-09-30'),
(4, 'Delta Marketing', 4, 300000.00, '2024-02-01', '2024-11-30'),
(5, 'Epsilon Research', 3, 100000.00, '2024-05-01', '2025-01-31');

-- (1) Write a 3-table JOIN showing employee name, department budget, and project budget
SELECT 
    e.name AS employee_name, 
    d.dept_budget, 
    p.budget AS project_budget
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id
JOIN projects p ON e.emp_id = p.lead_emp_id;

-- (2) Write a query showing departments where total project budget exceeds department budget
SELECT 
    d.dept_name, 
    SUM(p.budget) AS total_project_budget,
    d.dept_budget
FROM departments d
JOIN employees e ON d.dept_id = e.dept_id
JOIN projects p ON e.emp_id = p.lead_emp_id
GROUP BY 
    d.dept_name, 
    d.dept_budget
HAVING SUM(p.budget) > d.dept_budget;
