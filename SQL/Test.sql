create database clg;
use clg;
create table student (
	id int primary key,
    stu_name varchar(1000),
    age int not null
);
insert into student values(1,"Aman",12);
insert into student values(2,"Sham",13);
select * from student;