CREATE DATABASE employee_tracker;

USE employee_tracker;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    joining_date DATE,
    email VARCHAR(100)
);

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY,
    employee_id INT,
    date DATE,
    clock_in TIME,
    clock_out TIME,
    status VARCHAR(20),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

CREATE TABLE tasks (
    task_id INT PRIMARY KEY,
    employee_id INT,
    tasks_completed INT,
    hours_spent INT,
    task_date DATE,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);

SELECT * FROM employees;

SELECT * FROM attendance;

SELECT * FROM tasks;

-- 1. INSERT QUERY
INSERT INTO employees
VALUES (121, 'Zerubba', 'IT', '2024-01-15', 'zerubba@gmail.com');
SELECT * FROM employees;

-- 2. UPDATE QUERY
UPDATE employees SET department = 'HR' WHERE employee_id = 121;
SELECT * FROM employees WHERE employee_id = 121;

-- 3. DELETE QUERY
DELETE FROM employees WHERE employee_id = 121;
SELECT * FROM employees;

-- 4. FILTER QUERY
SELECT * FROM attendance
WHERE status = 'Absent';

-- 5. SORTING QUERY
SELECT * FROM tasks
ORDER BY tasks_completed DESC;

-- 6. JOIN QUERY
SELECT 
    e.employee_name,
    e.department,
    a.status
FROM employees e
JOIN attendance a
ON e.employee_id = a.employee_id;

-- 7. STORED PROCEDURE
DELIMITER //

CREATE PROCEDURE GetTotalWorkHours()
BEGIN
    SELECT 
        employee_id,
        SUM(hours_spent) AS total_hours
    FROM tasks
    GROUP BY employee_id;
END //

DELIMITER ;
CALL GetTotalWorkHours();

-- 8. VIEWS
CREATE VIEW employee_productivity_view AS
SELECT 
    e.employee_name,
    e.department,
    t.tasks_completed,
    t.hours_spent
FROM employees e
JOIN tasks t
ON e.employee_id = t.employee_id;
SELECT * FROM employee_productivity_view;
