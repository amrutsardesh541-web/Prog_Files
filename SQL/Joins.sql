show databases;
create database colleges;
use colleges;
create table student(
	sid int primary key,
    sname varchar(100),
    city varchar(100)
);
create table department(
	did int primary key,
    dname varchar(100),
    intake int 
);
alter table student
add column did int;

alter table student 
add constraint fk foreign key (did) references department(did);

insert into department
values
(1,"EXTC",100),
(2,"AIDS",200),
(3,"Comp",100);

insert into student
values
(101,"ABC","Pune",1),
(102,"DEF","Mumbai",2),
(103,"XYZ","Nashik",2);

-- inner join
select * from student as stu
inner join department as dept
on stu.did = dept.did;

-- right join (here department is right)
select * from student as stu
right join department as dept
on stu.did = dept.did;

-- left join (here student is left)
select * from student as stu
left join department as dept
on stu.did = dept.did;

-- full join full outer iis deprecated
/*
You don't have full joins in MySQL, but you can sure emulate them.

For a code sample transcribed from this Stack Overflow question you have:

With two tables t1, t2:

INSTEAD USE THE BELOW CODE

SELECT * FROM t1
LEFT JOIN t2 ON t1.id = t2.id
UNION
SELECT * FROM t1
RIGHT JOIN t2 ON t1.id = t2.id
*/


