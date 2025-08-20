show databases;
use hospital;
show tables;
desc doctor;
select * from doctor;
insert into doctor
values
(9,'Rajesh Padwi','MBBS MD', 'Sexologist', 145000);
select * from doctor;

-- display doc details who are gynaec
select * from doctor
where speciality = 'Gynecology';

-- remove a particular row
select * from patients;
delete from patients
where p_id = 101;
select * from patients;

set sql_safe_updates = 0;
-- update row values
select * from doctor;
update doctor
set salary = salary + 50000;
select * from patients;

-- add column
alter table patients
add column address varchar(100);
select * from patients;

-- rename columns
alter table patients
change column disease ilness varchar(100);
select * from patients;

-- truncate table
create table test(
_id int,
field varchar(10)
);
insert into test
values
(1,'Ram');
select * from test;
truncate table test;
select * from test;

-- delete entire table
drop table test;


