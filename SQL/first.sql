CREATE DATABASE IF NOT EXISTS college; 
CREATE DATABASE IF NOT EXISTS xyz;

DROP DATABASE IF EXISTS xyz;
USE college;

CREATE TABLE student(
roll_no INT,
name VARCHAR(30),
age INT
);

INSERT INTO student VALUES
(101, "ali", 14),
(102, "ahmad",16);

SELECT * FROM student;

SHOW DATABASES;
USE college;
SHOW TABLES;

CREATE DATABASE IF NOT EXISTS instagram; 
USE instagram;

CREATE TABLE user(
id INT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
age INT,
email VARCHAR(50) UNIQUE,
followers INT DEFAULT 0,
following INT,
CONSTRAINT age_check CHECK (age >= 13)
);

CREATE TABLE post(
id INT primary key,
content VARCHAR(100),
user_id INT,
foreign key (user_id) references user(id)
);

INSERT INTO user
(id, age, name, email, followers, following)
VALUES
(1, 14, "adam", "adam@yahoo.in", 123, 145),
(2, 15, "bob", "bob123@gmail.com", 200, 200),
(3, 16, "casey", "casey@email.com", 300, 306),
(4, 17, "donald", "donald@gmail.com", 200, 105);

select * from user;

set sql_safe_updates = 0;


select @@autocommit;
set autocommit =0;
set autocommit =1;