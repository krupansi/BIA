create database test;
USE test;

CREATE TABLE Employee
(EmpId INT auto_increment PRIMARY KEY,
FirstName VARCHAR(200),
LastName VARCHAR(200),
Age INT,
Department VARCHAR(100),
City VARCHAR(255),
Salary DECIMAL(10, 2) );

SELECT * FROM Employee;

INSERT INTO Employee (FirstName, LastName, Age, Department, City, Salary) Values 
('Krupa', 'Hirpara', 22, 'AI', 'Vadodara', 100000.00), 
('Montu', 'Patel', 25, 'ML', 'Surat', 50000.00),
('Ritul', 'Joshi', 30, 'Data Engineer', 'Ahemdabad', 25000.00),
('Jensi', 'Parmar', 28, 'AI', 'Vadodara', 80000.00);

DELETE FROM Employee WHERE EmpId='14' & '15';


