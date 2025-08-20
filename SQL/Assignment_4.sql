CREATE DATABASE Company;
CREATE TABLE Employee(
	emp_no int primary key,
    emp_name varchar(50),
    join_date date,
    designation varchar(50),
    salary bigint not null
);
INSERT INTO Employee (emp_no, emp_name, join_date, designation, salary) 
VALUES 
(1, 'Rajesh Kumar', '2000-12-12', 'Manager', 1200000),
(2, 'Anita Sharma', '2001-11-11', 'Developer', 900000),
(3, 'Sanjay Gupta', '2002-10-10', 'Analyst', 800000),
(4, 'Priya Reddy',  '2000-09-09', 'Tester', 700000),
(5, 'Amitabh Bhattacharya', '2004-05-11', 'Designer', 1000000);

-- implicit
DELIMITER //
CREATE PROCEDURE DISPLAY()
BEGIN
DECLARE rows_affected int;
SELECT * FROM Employee;
SELECT COUNT(*) FROM Employee;
END//
DELIMITER ;
DELIMITER //

-- explicit cursor
CREATE PROCEDURE Highest_Sal()
BEGIN
DECLARE 
DECLARE HIGH CURSOR FOR
SELECT * from Employee
ORDER BY salary DESC
LIMIT 5;


END//


