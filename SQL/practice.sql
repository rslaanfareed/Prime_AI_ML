CREATE DATABASE Company;

USE Company;

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50),
    Location VARCHAR(50)
);

CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Salary DECIMAL(10,2),
    HireDate DATE,
    DepartmentID INT,
    ManagerID INT,
    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

CREATE TABLE Projects (
    ProjectID INT PRIMARY KEY,
    ProjectName VARCHAR(100),
    Budget DECIMAL(12,2),
    DepartmentID INT,
    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

INSERT INTO Departments VALUES
(1,'IT','New York'),
(2,'HR','Chicago'),
(3,'Finance','Boston'),
(4,'Marketing','Dallas');

INSERT INTO Employees VALUES
(101,'Alice','Johnson',7000,'2020-01-10',1,NULL),
(102,'Bob','Smith',5500,'2021-04-15',1,101),
(103,'Charlie','Brown',4800,'2022-02-20',2,NULL),
(104,'David','Wilson',6200,'2019-07-05',3,NULL),
(105,'Emma','Davis',5100,'2023-03-18',4,NULL),
(106,'Frank','Taylor',5800,'2020-11-12',3,104),
(107,'Grace','Thomas',4500,'2022-06-01',2,103),
(108,'Henry','Moore',7600,'2018-08-25',1,101);

INSERT INTO Projects VALUES
(201,'Payroll System',250000,1),
(202,'Recruitment Portal',100000,2),
(203,'Budget Analysis',300000,3),
(204,'Social Media Campaign',180000,4),
(205,'Cyber Security',450000,1);


-- Display employee name and department name.
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
JOIN Departments d
ON e.DepartmentID=d.DepartmentID;


-- Display employee salary and department location.
SELECT e.FirstName, e.LastName, e.Salary, d.Location as Dep_Loc
FROM Employees e
JOIN Departments d
ON e.DepartmentID=d.DepartmentID;


-- Display all projects with department names.
SELECT p.ProjectName, d.DepartmentName
FROM Projects p
JOIN Departments d
ON p.DepartmentID=d.DepartmentID;


-- Display employees working in IT department.
SELECT e.FirstName, e.LastName, d.DepartmentName
FROM Employees e
JOIN Departments d
ON e.DepartmentID=d.DepartmentID
Where d.DepartmentName = 'IT';


-- Display employees and their managers.
SELECT CONCAT(e.FirstName," ",e.LastName) AS EMPLOYEE, CONCAT(m.FirstName," ",m.LastName) AS MANAGER
FROM Employees e
JOIN Employees m
ON e.EmployeeID=m.ManagerID;


-- Display managers and the employees they supervise.
SELECT CONCAT(m.FirstName," ",m.LastName) AS SUPERVISOR, CONCAT(e.FirstName," ",e.LastName) AS SUPERVISED
FROM Employees m
JOIN Employees e
ON e.EmployeeID=m.ManagerID;


-- Display employees even if they don't have managers.
SELECT CONCAT(e.FirstName," ",e.LastName) AS EMPLOYEE, CONCAT(m.FirstName," ",m.LastName) AS MANAGER
FROM Employees e
LEFT JOIN Employees m
ON e.EmployeeID=m.ManagerID;


-- Display departments that have no employees
SELECT d.DepartmentName,COUNT(EmployeeID)
FROM Departments d
LEFT JOIN Employees e
ON d.DepartmentID=e.DepartmentID
GROUP BY d.DepartmentName
HAVING COUNT(*)=0;


-- Display every employee and every project in their department.
SELECT CONCAT(e.FirstName," ",e.LastName) AS EMPLOYEE, p.ProjectName, d.DepartmentName
FROM Departments d
JOIN Employees e ON d.DepartmentID=e.DepartmentID
JOIN Projects p ON d.DepartmentID=p.DepartmentID;


-- Display highest paid salary of every department.
SELECT d.DepartmentName,MAX(Salary)
FROM Departments d
join Employees e
ON d.DepartmentId=e.DepartmentID
GROUP BY d.DepartmentName;


-- Procedure to display employees by department.
Delimiter $$
CREATE PROCEDURE display_by_department(IN DepartmentID INT)
BEGIN
SELECT d.DepartmentName, CONCAT(e.FirstName," ",e.LastName) AS EMPLOYEE
FROM Employees e
JOIN Departments d 
ON e.DepartmentID=d.DepartmentID;

END $$
Delimiter ;


-- DROP PROCEDURE display_by_department;

CALL display_by_department(2);
