#create database TC;
use TC;

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

create view place_view as
select place_id, city, state, type_ from place;

select * from place_view;

create view customer_interest as
select cust_name, city, interest from customer;

select * from customer_interest;

create view customer_reservation as
select c.cust_name, c.city, b.fee from customer as c
inner join booking as b 
on c.cust_id = b.c_id;

select * from customer_reservation;

select * from place_view;
insert into place_view values
(6, 'Darjelling', 'West Bengal', 'Hill Station'); 


update place_view
set state = 'Meghalaya'
where state = 'West Bengal';
