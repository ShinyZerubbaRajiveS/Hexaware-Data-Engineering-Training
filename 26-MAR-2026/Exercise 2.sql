CREATE DATABASE capstone_sql;
USE capstone_sql;

CREATE TABLE students (     
student_id INT PRIMARY KEY,     
student_name VARCHAR(100),    
city VARCHAR(50),     
age INT ); 

CREATE TABLE enrollments (     
enrollment_id INT PRIMARY KEY,     
student_id INT,     
course_name VARCHAR(100),     
trainer VARCHAR(100),    
fee DECIMAL(10,2) ); 

INSERT INTO students VALUES (1,'Aarav Sharma','Hyderabad',22), (2,'Priya Reddy','Bangalore',23), (3,'Rahul Verma','Mumbai',24), (4,'Sneha Kapoor',NULL,21), (5,'Vikram Singh','Chennai',25), (6,NULL,'Delhi',22);

INSERT INTO enrollments VALUES (101,1,'MySQL','Abdullah Khan',5000), (102,1,'Python','Abdullah Khan',7000), (103,2,'Power BI','Kiran',6000), (104,3,'Azure Data Factory','Sneha',8000), (105,NULL,'Excel','Rohan',3000), (106,8,'Databricks','Ananya',9000);

-- Exercise 1
select s.student_name,e.course_name
from students s inner join enrollments e
on s.student_id=e.student_id;

-- Exercise 2
select s.student_id, s.student_name,e.course_name
from students s left join enrollments e
on s.student_id=e.student_id;

-- Exercise 3
select s.student_name,e.course_name
from students s right join enrollments e
on s.student_id=e.student_id;

-- Exercise 4
select s.student_name,e.course_name
from students s left join enrollments e
on s.student_id=e.student_id
union
select s.student_name,e.course_name
from students s right join enrollments e
on s.student_id=e.student_id;

-- Exercise 5
select s.student_name,e.course_name
from students s cross join enrollments e;

-- Exercise 6
select s.student_name,s.city,e.course_name
from students s inner join enrollments e on s.student_id=e.student_id
where s.city='Hyderabad';

-- Exercise 7
select s.student_name,e.course_name,e.fee
from students s right join enrollments e on s.student_id=e.student_id
where e.fee>6000;

-- Exercise 8
select s.student_name,count(e.course_name) as totalCoursesPerStudent
from students s left join enrollments e on s.student_id=e.student_id
group by s.student_name;

-- Exercise 9
select s.student_id,s.student_name,sum(e.fee) as totalFeePerStudent
from students s left join enrollments e on s.student_id=e.student_id
group by s.student_id,s.student_name;

-- Exercise 10
select s.student_name,count(e.course_name) as TotalCoursesEnrolled
from students s left join enrollments e on s.student_id=e.student_id
group by s.student_name having count(e.course_name)>1;

-- Exercise 11
select e.trainer,sum(e.fee) as totalFee
from enrollments e group by e.trainer having sum(e.fee)>10000;

-- Exercise 12
select city,count(student_id) as totalStudents
from students group by city having count(student_id)>1;

-- Exercise 13 (Capstone query)
select  s.student_name,s.city,sum(e.fee) as totalFee
from students s inner join enrollments e on s.student_id=e.student_id
group by s.student_name,s.city having sum(e.fee)>5000
order by totalFee desc;