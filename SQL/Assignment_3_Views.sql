create database TouringCompany;
use TouringCompany;
drop database TouringCompany;
create database Touring2;
use Touring2;
create table place (
	place_id int primary key auto_increment,
    city varchar(50),
    state varchar(50),
    season varchar(50),
    type_ varchar(50)
)auto_increment=1;

-- Insert 5 records into the place table
insert into place (city, state, season, type_)
values
('Manali', 'Himachal Pradesh', 'Winter', 'Hill Station'),
('Jaipur', 'Rajasthan', 'Winter', 'Historical'),
('Goa', 'Goa', 'Summer', 'Beach'),
('Allapuzha', 'Kerala', 'Monsoon', 'Backwaters'),
('Leh', 'Ladakh', 'Summer', 'Adventure');

select * from place;

create table customer (
	cust_id int,
    cust_name varchar(50),
    city varchar(50),
    phone bigint not null,
    email varchar(50), 
    interest varchar(50)
);

alter table customer
add primary key(cust_id);

-- Insert 5 records into the customer table
insert into customer 
values
(100,'Amit Sharma', 'Mumbai', 9876543210, 'amit@example.com', 'Adventure'),
(101,'Neha Singh', 'Delhi', 9876543211, 'neha@example.com', 'Historical'),
(102,'Raj Patel', 'Ahmedabad', 9876543212, 'raj@example.com', 'Beach'),
(103,'Priya Mehta', 'Bangalore', 9876543213, 'priya@example.com', 'Hill Station'),
(104,'Ravi Kumar', 'Chennai', 9876543214, 'ravi@example.com', 'Backwaters');

select * from customer;

create table booking(
	book_id int,
    c_id int,
    p_id int,
    fee bigint,
    nof_person int not null,
    from_ varchar(50)
);

alter table booking
add primary key(book_id),
add constraint fk0 foreign key(c_id) references customer(cust_id),
add constraint fk1 foreign key(p_id) references place(place_id);

insert into booking 
values
(200,100, 5, 50000, 2, '2024-08-01'),
(201,101, 2, 30000, 1, '2024-09-10'),
(202,102, 3, 40000, 4, '2024-10-15'),
(203,103, 1, 25000, 2, '2024-11-05'),
(204,104, 4, 35000, 3, '2024-12-20');

select * from booking;

-- create view having place_id, city, type, state
create view Place_of_Interest as
select place_id, city, type_, state from place;

select * from Place_of_Interest;

-- create a view which will display cust_name and names of cities of their interest
create view customer_info as
select cust_name, city, interest from customer;

select * from customer_info;

-- create a view which will display cust_name, city he has booked along with the fees he has paid
create view booking_info as 
select c.cust_name, c.city, b.fee from customer as c
join booking as b on c.cust_id = b.c_id;

select * from booking_info;

-- add a record in places using Place_of_Interest
insert into Place_of_Interest
values (6,'Chennai','Tamil Nadu','Urban');

select * from Place_of_Interest;

-- change the state of a particular city in places table using Place_of_Interest
update Place_of_Interest
set state = 'West Bengal'
where city = 'Jaipur';

select * from Place_of_Interest;
select * from place;

set sql_safe_updates = 0;

describe booking_info;