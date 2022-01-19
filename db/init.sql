CREATE DATABASE Python;
use Python;

CREATE TABLE user( uid int NOT NULL AUTO_INCREMENT, 
 name varchar(45) NOT NULL, 
 city varchar(35) NOT NULL,  
 age int NOT NULL,  
 PRIMARY KEY (uid));
 
INSERT INTO user (name, city,age) VALUES ("Yash", "Vadodara",21);