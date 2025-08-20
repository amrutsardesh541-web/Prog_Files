create database company;
use company;
/*
create table department(
	dept_id int primary key auto_increment,
    dept_name varchar(100) not null
);
*/
create table emp(
	e_id int primary key auto_increment,
    f_name varchar(20) not null,
    l_name varchar(20) not null,
    #foreign key (d_id) references department(dept_id),
    dept_name varchar(50) not null,
    salary bigint default 25000
);

INSERT INTO emp (f_name, l_name, dept_name, salary) VALUES
('John', 'Doe', 'HR', 30000),
('Jane', 'Smith', 'Finance', 45000),
('Alice', 'Brown', 'IT', 40000),
('Bob', 'Johnson', 'Marketing', 35000),
('Charlie', 'Williams', 'HR', 30000),
('Emily', 'Davis', 'Finance', 42000),
('Frank', 'Miller', 'IT', 39000),
('Grace', 'Wilson', 'Marketing', 34000),
('Hannah', 'Taylor', 'HR', 31000),
('Isaac', 'Anderson', 'Finance', 46000),
('Jack', 'Thomas', 'IT', 38000),
('Karen', 'Jackson', 'Marketing', 37000),
('Liam', 'White', 'HR', 29000),
('Mia', 'Harris', 'Finance', 43000),
('Noah', 'Martin', 'IT', 41000),
('Olivia', 'Thompson', 'Marketing', 33000),
('Peter', 'Garcia', 'HR', 32000),
('Quinn', 'Martinez', 'Finance', 44000),
('Rachel', 'Robinson', 'IT', 39500),
('Sam', 'Clark', 'Marketing', 36500),
('Tina', 'Rodriguez', 'HR', 30500),
('Uma', 'Lewis', 'Finance', 47000),
('Victor', 'Lee', 'IT', 40000),
('Wendy', 'Walker', 'Marketing', 36000),
('Xander', 'Hall', 'HR', 31500);

-- details of sales dept
select * from emp 
where dept_name = 'IT';

select * from emp;

-- update salary
update emp
set salary = salary + 15000
where e_id = 3;
select * from emp;

delete from emp
where e_id = 25;

select * from emp;

insert into emp
values
(25,'Randy','Ortan','IT',47000);
select * from emp;

-- find average salary
select dept_name, avg(salary) from emp
group by(dept_name);

-- list name of emps which earn greater than avg salary
select * from emp 
where salary > (select avg(salary) from emp);

-- retrieve who work in wither it or finance
select * from emp
where dept_name = 'IT' or dept_name = 'Finance';

-- retireve full name
select concat(f_name,' ',l_name) as full_name, dept_name, salary from emp;

-- use in operator
select * from emp
where dept_name in ('HR', 'IT');

-- starting with words
select * from emp
where l_name like 'M%';

-- return count
select dept_name, count(f_name) from emp
group by dept_name
order by dept_name desc;

select * from emp
where dept_name not in ('Marketing');

select dept_name, max(salary) from emp
group by dept_name
order by dept_name  asc;

-- range
select * from emp
where salary between 45000 and 60000;