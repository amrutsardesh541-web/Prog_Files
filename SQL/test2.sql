-- create a database
CREATE DATABASE Hospital;
-- list all databases
SHOW DATABASES;

USE Company;
-- Create the EMP table with a default value for SALARY
CREATE TABLE EMP1 (
    EMP_ID INT PRIMARY KEY AUTO_INCREMENT,
    F_NAME VARCHAR(100) NOT NULL,
    L_NAME VARCHAR(100) NOT NULL,
    DEPT VARCHAR(100) NOT NULL,
    SALARY BIGINT DEFAULT 25000
);

-- Insert a record with NULL for SALARY
INSERT INTO EMP1 (F_NAME, L_NAME, DEPT) VALUES
('John', 'Doe', 'HR');

-- Check the table
SELECT * FROM EMP1;
