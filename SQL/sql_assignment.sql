-- Create Database
CREATE DATABASE CompanyDB;

-- Use Database
USE CompanyDB;

-- Create Employee Table
CREATE TABLE Employee (
    EmpID INT PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Department VARCHAR(50) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL,
    HireDate DATE NOT NULL
);

-- Insert Records
INSERT INTO Employee (EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES
(101, 'Alice',  'Johnson',  'IT',        6500, '2020-03-15'),
(102, 'Mark',   'Rivera',   'HR',        4800, '2019-07-22'),
(103, 'Sophia', 'Lee',      'Finance',   7200, '2021-01-10'),
(104, 'Daniel', 'Kim',      'IT',        5800, '2018-11-05'),
(105, 'Emma',   'Brown',    'Marketing', 5300, '2022-04-18'),
(106, 'Liam',   'Patel',    'Finance',   6900, '2020-09-29'),
(107, 'Olivia', 'Garcia',   'HR',        4600, '2017-06-30'),
(108, 'Noah',   'Thompson', 'IT',        7500, '2023-02-12'),
(109, 'Ava',    'Martinez', 'Marketing', 5100, '2019-12-02'),
(110, 'Ethan',  'Davis',    'Finance',   8000, '2016-05-14');



-- Q1. Write a query to display every employee and all their data.
SELECT * FROM Employee;


-- Q2. List only the FirstName, LastName, and Salary of every employee.
SELECT FirstName,LastName,Salary FROM Employee;


-- Q3. Show all employees who work in the 'IT' department.
SELECT * FROM Employee
WHERE Department = "IT";


-- Q4. Retrieve employees with a salary greater than 6000.
SELECT * FROM Employee
WHERE Salary > 6000;


-- Q5. List all employees ordered by HireDate from newest to oldest
SELECT * FROM Employee
ORDER BY HireDate DESC;


-- Q6. Show a list of all unique departments present in the table.
SELECT DISTINCT Department FROM Employee;


-- Q7. Find employees whose first name starts with ‘Aʼ
SELECT * FROM Employee 
WHERE FirstName Like 'A%';


-- Q8. Show employees whose salaries are between 4000 and 7000.
SELECT * FROM Employee
WHERE Salary BETWEEN 4000 AND 7000;


-- Q9. Find the average salary of all employees.
SELECT AVG(Salary) FROM Employee;


-- Q10. List each department along with the number of employees, but only include departments with more than 2 employees
SELECT Department, Count(*) AS emp_count
FROM Employee
GROUP BY Department
HAVING Count(*)>2;


-- Show employees not working in HR.
SELECT * FROM Employee
WHERE Department != "HR";


-- Find employees hired before 2020.
SELECT * FROM Employee
WHERE HireDate < '2020-01-01';


-- Find employees hired during 2020.
SELECT * FROM Employee
WHERE HireDate LIKE '2020%';


-- Display employees whose last name contains 'son'.
SELECT * FROM Employee
WHERE LastName LIKE '%son';


-- Find employees hired in March (regardless of year).
SELECT * FROM Employee
WHERE HireDate LIKE '____-03-__';


-- Display employees whose salary is divisible by 1000.
SELECT * FROM Employee
WHERE Salary%1000=0;


-- Show employees whose department starts with F or ends with g.
SELECT * FROM Employee
WHERE Department LIKE 'F%' OR Department LIKE '%g';


-- Display employee name and salary after a 10% raise.
SET sql_safe_updates=0;
UPDATE Employee
SET Salary=Salary+Salary*0.1;
SELECT FirstName,LastName, Salary FROM Employee;


-- Display employee name and salary after 15% tax deduction.
UPDATE Employee
SET Salary=Salary-Salary*0.15;
SELECT FirstName,LastName, Salary FROM Employee;


-- Display employee full name in one column.
SELECT CONCAT(FirstName," ",LastName) AS Name
From Employee;


-- Display full name in uppercase.
SELECT UPPER(CONCAT(FirstName," ",LastName)) AS Name
From Employee;


-- Display first 3 letters of every employee's first name.
SELECT LEFT(FirstName, 3) AS short_name FROM employee;


-- Calculate years each employee has worked in the company.
SELECT FirstName, LastName, ROUND(DATEDIFF(CURDATE(), HireDate) / 365, 1) AS years
FROM employee;


-- Display departments where average salary exceeds 6000.
SELECT Department,AVG(Salary) AS Average_Salary
FROM Employee
GROUP BY Department
HAVING AVG(Salary) > 6000;


-- Display departments whose highest salary exceeds 7000.
SELECT Department,MAX(Salary) AS Max_Salary
FROM Employee
GROUP BY Department
HAVING MAX(Salary) > 7000;


-- Display full name as Johnson, Alice
SELECT CONCAT(LastName,", ", FirstName) AS Name
From employee;


-- Find employees hired on Monday.
SELECT FirstName, HireDate
FROM employee
WHERE WEEKDAY(HireDate) = 0;


-- Find employees earning above average salary.
SELECT * FROM Employee
WHERE Salary > (Select AVG(Salary) From Employee);


-- Display department(s) with highest average salary.
SELECT Department,AVG(Salary) From Employee
Group by Department
Order by AVG(Salary) DESC;


-- Display employees whose salary is greater than the company average but less than the maximum salary.
SELECT FirstName,Department,Salary From Employee
WHERE Salary >(Select AVG(Salary) From Employee) AND Salary<(Select Max(Salary) From Employee);



SELECT * FROM Employee;
