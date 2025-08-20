show databases;
create database trig_ass;
use trig_ass;

create table employ(
	emp_id int primary key,
    emp_name varchar(30),
    designation varchar(30)
);

insert into employ 
values
(1,'wer','Manager'),
(2,'sdf','Clerk'),
(3,'pdf','CEO');

create table employ_audit(
	emp_id int primary key,
    emp_name varchar(30),
    designation varchar(30),
	operation varchar(30),
    timeofday timestamp default current_timestamp
);

delimiter //
create trigger update_trig 
before update on employ for each row
begin
insert into employ_audit (emp_id, emp_name, designation, operation) 
values(old.emp_id, old.emp_name, old.designation, 'UPDATE');
end//
delimiter ;

update employ
set designation = 'Sr.Clerk'
where emp_id = 2;

select * from employ_audit;

delimiter //
create trigger delete_trig 
before delete on employ for each row
begin
insert into employ_audit (emp_id, emp_name, designation, operation) 
values(old.emp_id, old.emp_name, old.designation, 'DELETE');
end//
delimiter ;

delete from employ
where emp_id = 3;

select * from employ_audit;

delimiter //
create trigger insert_trig 
before insert on employ for each row
begin
insert into employ_audit (emp_id, emp_name, designation, operation) 
values(new.emp_id, new.emp_name, new.designation, 'INSERT');
end//
delimiter ;

insert into employ 
values
(4,'jado','CEO');

select * from employ_audit;
