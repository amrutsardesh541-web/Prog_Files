#create database clg;
#use clg;
-- create necessary tables

create table department (
	dept_id varchar(10) primary key,
    d_name varchar(50),
    hod_id varchar(10) not null,
    intake int not null
);
alter table department
add column asset bigint not null;
describe department;

-- insert values in department

insert into department (dept_id, d_name, hod_id, intake, asset) values
('CSE', 'Computer Science', 'E001', 120, 50000000),
('ECE', 'Electronics', 'E002', 90, 30000000),
('MECH', 'Mechanical', 'E003', 80, 40000000),
('CIV', 'Civil', 'E004', 70, 35000000),
('IT', 'Information Technology', 'E005', 100, 45000000),
('EEE', 'Electrical', 'E006', 75, 32000000),
('CHEM', 'Chemical', 'E007', 60, 27000000),
('BIO', 'Biotechnology', 'E008', 50, 25000000),
('AERO', 'Aeronautical', 'E009', 40, 20000000),
('AUTO', 'Automobile', 'E010', 45, 22000000),
('ARCH', 'Architecture', 'E011', 30, 18000000),
('MATH', 'Mathematics', 'E012', 25, 15000000),
('PHYS', 'Physics', 'E013', 20, 14000000),
('AIDS', 'Artificial Intelligence and Data Science', 'E014', 22, 16000000),
('META', 'Metallurgy', 'E015', 35, 21000000);

select * from department;

create table student (
	stu_id varchar(10) primary key,
    s_name varchar(50) not null,
    DOB date not null,
    city varchar(50),
    dept_id varchar(10) not null,
    foreign key (dept_id) references department(dept_id)
);

-- inset values in student table
insert into student (stu_id, s_name, DOB, city, dept_id) values
('S001', 'Aarav Sharma', '2002-01-15', 'Pune', 'CSE'),
('S002', 'Bhavya Mehta', '2002-05-22', 'Mumbai', 'CSE'),
('S003', 'Charvi Desai', '2001-11-30', 'Nashik', 'ECE'),
('S004', 'Divya Rao', '2002-03-10', 'Nagpur', 'ECE'),
('S005', 'Eshan Patel', '2002-08-19', 'Kolhapur', 'MECH'),
('S006', 'Falguni Roy', '2001-12-01', 'Pune', 'MECH'),
('S007', 'Gaurav Reddy', '2002-07-21', 'Mumbai', 'CIV'),
('S008', 'Harini Nair', '2002-09-25', 'Nashik', 'CIV'),
('S009', 'Ishaan Singh', '2001-10-13', 'Nagpur', 'IT'),
('S010', 'Jiya Kulkarni', '2002-04-29', 'Kolhapur', 'IT'),
('S011', 'Karan Verma', '2002-02-18', 'Pune', 'EEE'),
('S012', 'Lavanya Joshi', '2002-06-11', 'Mumbai', 'EEE'),
('S013', 'Meera Kulkarni', '2001-12-07', 'Nashik', 'CHEM'),
('S014', 'Nikhil Desai', '2002-08-15', 'Nagpur', 'CHEM'),
('S015', 'Ojas Deshmukh', '2002-10-19', 'Kolhapur', 'BIO'),
('S016', 'Prachi Pandey', '2001-11-22', 'Pune', 'BIO'),
('S017', 'Rahul Patil', '2002-05-25', 'Mumbai', 'AERO'),
('S018', 'Sneha Reddy', '2002-03-17', 'Nashik', 'AERO'),
('S019', 'Tanvi Rao', '2001-09-20', 'Nagpur', 'AUTO'),
('S020', 'Uday Kulkarni', '2002-07-14', 'Kolhapur', 'AUTO'),
('S021', 'Vaishali Nair', '2002-01-12', 'Pune', 'ARCH'),
('S022', 'Yash Mehta', '2002-08-30', 'Mumbai', 'ARCH'),
('S023', 'Zara Sharma', '2001-06-28', 'Nashik', 'MATH'),
('S024', 'Aman Gupta', '2002-10-08', 'Nagpur', 'MATH'),
('S025', 'Bharat Rao', '2002-04-04', 'Kolhapur', 'PHYS'),
('S026', 'Chetna Desai', '2001-09-13', 'Pune', 'PHYS'),
('S027', 'Deepak Iyer', '2002-03-26', 'Mumbai', 'CHEM'),
('S028', 'Esha Menon', '2002-07-17', 'Nashik', 'META'),
('S029', 'Farhan Khan', '2001-12-24', 'Nagpur', 'META'),
('S030', 'Gitanjali Roy', '2002-05-29', 'Kolhapur', 'META');

select * from student;

create table employee (
	emp_id varchar(10) primary key,
    e_name varchar(50) not null,
    date_o_b date not null,
    phone bigint not null,
    email_id varchar(50) unique,
    designation varchar(50) not null,
    dept_id varchar(10) not null,
    hod_id varchar(10),
    foreign key (dept_id) references department(dept_id)
);

-- insert into employee
insert into employee (emp_id, e_name, date_o_b, phone, email_id, designation, dept_id, hod_id) values
('A001', 'Dr. Rahul Verma', '1975-04-25', 9876543210, 'rahul.verma@viit.edu', 'Professor', 'CSE', 'E001'),
('A002', 'Dr. Neha Gupta', '1978-09-17', 9123456789, 'neha.gupta@viit.edu', 'Professor', 'ECE', 'E002'),
('A003', 'Dr. Ramesh Iyer', '1980-12-05', 9234567890, 'ramesh.iyer@viit.edu', 'Professor', 'MECH', 'E003'),
('A004', 'Dr. Suman Rao', '1982-07-14', 9345678901, 'suman.rao@viit.edu', 'Professor', 'CIV', 'E004'),
('A005', 'Dr. Priya Menon', '1976-11-23', 9456789012, 'priya.menon@viit.edu', 'Professor', 'IT', 'E005'),
('A006', 'Dr. Vikram Deshmukh', '1979-03-30', 9567890123, 'vikram.deshmukh@viit.edu', 'Professor', 'EEE', 'E006'),
('A007', 'Dr. Anjali Kapoor', '1981-08-18', 9678901234, 'anjali.kapoor@viit.edu', 'Professor', 'CHEM', 'E007'),
('A008', 'Dr. Ajay Nair', '1983-02-06', 9789012345, 'ajay.nair@viit.edu', 'Professor', 'BIO', 'E008'),
('A009', 'Dr. Manish Singh', '1977-10-27', 9890123456, 'manish.singh@viit.edu', 'Professor', 'AERO', 'E009'),
('A010', 'Dr. Pooja Sharma', '1984-06-15', 9901234567, 'pooja.sharma@viit.edu', 'Professor', 'AUTO', 'E010'),
('A011', 'Dr. Rajesh Kumar', '1975-07-25', 9871111210, 'rajesh.kumar@viit.edu', 'Professor', 'ARCH', 'E011'),
('A012', 'Dr. Sunita Patil', '1978-10-17', 9121111289, 'sunita.patil@viit.edu', 'Professor', 'MATH', 'E012'),
('A013', 'Dr. Vikas Desai', '1980-01-05', 9231111290, 'vikas.desai@viit.edu', 'Professor', 'PHYS', 'E013'),
('A014', 'Dr. Meena Sharma', '1982-04-14', 9341111301, 'meena.sharma@viit.edu', 'Professor', 'CHEM', 'E014'),
('A015', 'Dr. Alok Joshi', '1976-09-23', 9451111312, 'alok.joshi@viit.edu', 'Professor', 'META', 'E015'),
('A016', 'Prof. Veena Rao', '1985-05-20', 9561111413, 'veena.rao@viit.edu', 'Assistant Professor', 'CSE', NULL),
('A017', 'Prof. Rohan Mehta', '1987-02-11', 9671111424, 'rohan.mehta@viit.edu', 'Assistant Professor', 'ECE', NULL),
('A018', 'Prof. Nisha Singh', '1983-09-30', 9781111435, 'nisha.singh@viit.edu', 'Assistant Professor', 'MECH', NULL),
('A019', 'Prof. Vinay Kulkarni', '1986-12-19', 9891111446, 'vinay.kulkarni@viit.edu', 'Assistant Professor', 'CIV', NULL),
('A020', 'Prof. Amrita Iyer', '1988-07-07', 9901111457, 'amrita.iyer@viit.edu', 'Assistant Professor', 'IT', NULL),
('A021', 'Prof. Sumit Nair', '1982-08-15', 9871111518, 'sumit.nair@viit.edu', 'Assistant Professor', 'EEE', NULL),
('A022', 'Prof. Pranav Joshi', '1984-11-05', 9121111529, 'pranav.joshi@viit.edu', 'Assistant Professor', 'CHEM', NULL),
('A023', 'Prof. Kavita Reddy', '1981-03-12', 9231111530, 'kavita.reddy@viit.edu', 'Assistant Professor', 'BIO', NULL),
('A024', 'Prof. Ajay Singh', '1985-01-25', 9341111541, 'ajay.singh@viit.edu', 'Assistant Professor', 'AERO', NULL),
('A025', 'Prof. Swati Desai', '1986-02-14', 9451111552, 'swati.desai@viit.edu', 'Assistant Professor', 'AUTO', NULL),
('A026', 'Prof. Rajeev Nair', '1987-04-18', 9561111563, 'rajeev.nair@viit.edu', 'Assistant Professor', 'ARCH', NULL),
('A027', 'Prof. Monika Patil', '1988-07-12', 9671111574, 'monika.patil@viit.edu', 'Assistant Professor', 'MATH', NULL),
('A028', 'Prof. Rakesh Kulkarni', '1989-09-17', 9781111585, 'rakesh.kulkarni@viit.edu', 'Assistant Professor', 'PHYS', NULL),
('A029', 'Prof. Snehal Sharma', '1990-06-23', 9891111596, 'snehal.sharma@viit.edu', 'Assistant Professor', 'CHEM', NULL),
('A030', 'Prof. Alka Menon', '1982-10-29', 9901111607, 'alka.menon@viit.edu', 'Assistant Professor', 'META', NULL);

select * from employee;

create table company (
	comp_id varchar(10) primary key,
    comp_name varchar(50) not null,
    country varchar(100) not null
);

-- insert values into company
insert into company (comp_id, comp_name, country) values
('comp01', 'Tata Consultancy Services', 'India'),
('comp02', 'Infosys', 'India'),
('comp03', 'Wipro', 'India'),
('comp04', 'HCL Technologies', 'India'),
('comp05', 'Tech Mahindra', 'India'),
('comp06', 'Larsen & Toubro Infotech', 'India'),
('comp07', 'Mindtree', 'India'),
('comp08', 'Capgemini', 'France'),
('comp09', 'Accenture', 'Ireland'),
('comp10', 'Cognizant', 'United States');

select * from company;


create table placement_record(
	stu_id varchar(10) not null,
    comp_id varchar(10) not null,
    package bigint,
    designation varchar(100) not null,
    year_of_start year not null,
    foreign key (stu_id) references student(stu_id),
    foreign key (comp_id) references company(comp_id)
);

-- insert values in placement record
insert into placement_record (stu_id, comp_id, package, designation, year_of_start) values
('S001', 'comp01', 800000, 'Software Engineer', 2024),
('S002', 'comp01', 750000, 'System Analyst', 2024),
('S003', 'comp02', 850000, 'Software Developer', 2024),
('S004', 'comp02', 800000, 'Data Analyst', 2024),
('S005', 'comp03', 900000, 'Mechanical Engineer', 2024),
('S006', 'comp03', 850000, 'Design Engineer', 2024),
('S007', 'comp04', 950000, 'Civil Engineer', 2024),
('S008', 'comp04', 900000, 'Structural Engineer', 2024),
('S009', 'comp05', 920000, 'IT Consultant', 2024),
('S010', 'comp05', 870000, 'Network Engineer', 2024),
('S011', 'comp06', 980000, 'Electrical Engineer', 2024),
('S012', 'comp06', 920000, 'Power Systems Engineer', 2024),
('S013', 'comp07', 860000, 'Chemical Engineer', 2024),
('S014', 'comp07', 830000, 'Process Engineer', 2024),
('S015', 'comp08', 990000, 'Biotech Engineer', 2024),
('S016', 'comp08', 950000, 'Lab Technician', 2024),
('S017', 'comp09', 890000, 'Aerospace Engineer', 2024),
('S018', 'comp09', 860000, 'Flight Dynamics Engineer', 2024),
('S019', 'comp10', 930000, 'Automotive Engineer', 2024),
('S020', 'comp10', 880000, 'Vehicle Design Engineer', 2024),
('S021', 'comp01', 920000, 'Architect', 2024),
('S022', 'comp02', 890000, 'Urban Planner', 2024),
('S023', 'comp03', 870000, 'Mathematician', 2024),
('S024', 'comp04', 920000, 'Data Scientist', 2024),
('S025', 'comp05', 850000, 'Physicist', 2024),
('S026', 'comp06', 880000, 'Research Scientist', 2024),
('S027', 'comp07', 810000, 'Chemical Researcher', 2024),
('S028', 'comp08', 870000, 'Materials Scientist', 2024),
('S029', 'comp09', 920000, 'Metallurgist', 2024),
('S030', 'comp10', 950000, 'Materials Engineer', 2024);

select * from placement_record;


-- inner join
select * from student as stu
inner join department as dept
using(dept_id)
order by stu.stu_id asc;

select s.s_name, d.d_name, d.asset from student as s
inner join department as d
on s.dept_id = d.dept_id
where s.city = 'Pune';

select upper(e_name) from employee
where e_name like '%ma%'
order by e_name desc;

select * from placement_record as pr
left join student as s
on s.stu_id = pr.stu_id;

select * from placement_record
right join company
using(comp_id);

select * from student
inner join placement_record
using(stu_id)
where package = (select max(package) from placement_record);

select * from student
inner join placement_record
using(stu_id)
where dept_id = 'MECH' and package > 600000;

select * from student
inner join placement_record
using(stu_id)
inner join company
using(comp_id)
where comp_name = 'Infosys';