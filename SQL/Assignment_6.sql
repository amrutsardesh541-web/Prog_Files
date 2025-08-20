-- Create the database and switch to it
drop database Trig_asignment;
CREATE DATABASE Trig_asignment;
USE Trig_asignment;

-- Create the main employee table
CREATE TABLE employ_1(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    join_date DATE,
    designation VARCHAR(15),
    salary BIGINT
);

-- Create the audit table with operation_time as default current timestamp
CREATE TABLE employ_1_audit(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    join_date DATE,
    designation VARCHAR(15),
    salary BIGINT,
    operation_type VARCHAR(50),
    operation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data into the employ_1 table
INSERT INTO employ_1 
VALUES 
(101, 'Ganesh Deshmukh', '2022-03-01', 'Manager', 850000),
(102, 'Snehal Pawar', '2021-11-15', 'Developer', 550000),
(103, 'Vishal Patil', '2023-02-10', 'Analyst', 450000),
(104, 'Prajakta Shinde', '2020-07-18', 'HR', 400000),
(105, 'Sagar Joshi', '2019-09-30', 'Engineer', 600000);

-- View the data in employ_1 table
SELECT * FROM employ_1;

-- Create a trigger to log updates into employ_1_audit table
DELIMITER //
CREATE TRIGGER updated_trigger BEFORE UPDATE
ON employ_1 FOR EACH ROW
BEGIN
  INSERT INTO employ_1_audit (emp_id, emp_name, join_date, designation, salary, operation_type)
  VALUES (OLD.emp_id, OLD.emp_name, OLD.join_date, OLD.designation, OLD.salary, 'UPDATE');
END//
DELIMITER ;

-- Create a trigger to log deletions into employ_1_audit table
DELIMITER //
CREATE TRIGGER deleted_record BEFORE DELETE
ON employ_1 FOR EACH ROW
BEGIN
  INSERT INTO employ_1_audit (emp_id, emp_name, join_date, designation, salary, operation_type)
  VALUES (OLD.emp_id, OLD.emp_name, OLD.join_date, OLD.designation, OLD.salary, 'DELETE');
END//
DELIMITER ;

-- Update the designation for an employee
UPDATE employ_1
SET designation = 'Senior Manager'
WHERE emp_id = 101;

-- View the audit log after update
SELECT * FROM employ_1_audit;

-- Delete an employee record
DELETE FROM employ_1
WHERE emp_id = 102;

-- View the audit log after delete
SELECT * FROM employ_1_audit;

-- View remaining records in employ_1 table
SELECT * FROM employ_1;
