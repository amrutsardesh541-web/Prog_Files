SHOW DATABASES;
USE colleges;
CREATE TABLE student_course(
	Roll_no int primary key,
    Course varchar(50),
    Course_code varchar(10),
    Semester int,
    Total_mks int,
    Percentage float
);

-- Insert entries into the student_course table
INSERT INTO student_course (Roll_no, Course, Course_code, Semester, Total_mks, Percentage) VALUES
(1, 'Mathematics', 'MATH101', 1, 500, 95.00), 
(2, 'Physics', 'PHY102', 2, 500, 82.50), 
(3, 'Chemistry', 'CHEM103', 3, 480, 78.00), 
(4, 'Biology', 'BIO104', 4, 470, 73.25), 
(5, 'Computer Science', 'CS105', 5, 460, 68.50), 
(6, 'History', 'HIS106', 6, 450, 65.75), 
(7, 'Geography', 'GEO107', 7, 440, 58.00), 
(8, 'English', 'ENG108', 8, 430, 52.40), 
(9, 'Economics', 'ECO109', 2, 420, 48.50), 
(10, 'Political Science', 'PS110', 1, 410, 45.20); 

select * from student_course;

delimiter //
create procedure show_num_stu(course_name varchar(50))
begin
declare range_80_100 int;
declare range_79_70 int;
declare range_69_60 int;
declare range_59_50 int;
declare range_below_49 int;
select count(*) into range_80_100 from student_course
where course = course_name and Percentage between 80 and 100;
select count(*) into range_79_70 from student_course
where course = course_name and Percentage between 70 and 79;
select count(*) into range_69_60 from student_course
where course = course_name and Percentage between 69 and 60;
select count(*) into range_59_50 from student_course
where course = course_name and Percentage between 59 and 50;
select count(*) into range_below_49 from student_course
where course = course_name and Percentage < 49;

select concat('80-100% : ', range_80_100) as 'Range 80-100',
concat('79-70% : ', range_79_70) as 'Range 79-70',
concat('69-60% : ', range_69_60) as 'Range 69-60',
concat('59-50% : ', range_59_50) as 'Range 59-50',
concat('below 49 : ', range_below_49) as 'Range Below 49';

end//
delimiter ;

call show_num_stu('mathematics');

drop procedure show_num_stu;
