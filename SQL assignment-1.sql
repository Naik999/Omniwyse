CREATE DATABASE MOVIE_RENTAL_STORE;
USE MOVIE_RENTAL_STORE;

CREATE TABLE films_data(
id INT PRIMARY KEY,
film_name varchar(50),
actor_name varchar(60),
length int ,
due int,
category varchar(20));

INSERT INTO films_data VALUES
(1001, 'bahubali',' prabhas raju Uppalapati',180,5000,'action'),
(1002, 'kgf','yash gowda',195,4000,'action'),
(1003, 'sahoo',' prabhas raju Uppalapati',180,5500,'love_action'),
(1004,'rrr','Taraka Rama Rao Jr Nandamuri',210,5600,' period action'),
(1005,'temper','Taraka Rama Rao Jr Nandamuri',175,3500,'love'),
(1006,'kalki',' prabhas raju Uppalapati',215,6000,'action thriller');

create table actors(
id int primary key,
first_name varchar(50),
last_name varchar(50),
movies varchar(200),
movie_id int,
foreign key(movie_id)references films_data(id)
);

 
INSERT INTO actors values
( 1 , ' prabhas raju','Uppalapati','bahubali', 1001),
( 2 , 'yash','gowda','kgf',1002),
( 3 , ' prabhas raju','Uppalapati','sahoo', 1003),
( 4, 'Taraka Rama Rao Jr','Nandamuri','rrr',1004),
( 5, 'Taraka Rama Rao Jr','Nandamuri','temper',1005),
( 6 , ' prabhas raju','Uppalapati','sahoo', 1006);

use movie_rental_store;

CREATE TABLE cus_data
(
   id INT PRIMARY KEY,
  name varchar(50),
  movie_no  int,
  rent int,
  foreign key(movie_no) references films_data(id)
); 

insert into cus_data values
(10,'ram',1001,5000),
(12,'sam',1002,4000);

  
 #1Q 
select * from actors where first_name = 'Taraka Rama Rao Jr';
#2Q
select * from actors where last_name = 'gowda';
#3Q
select distinct last_name from actors; 
#4Q
select last_name from actors group by last_name having count(last_name)<2;
#5Q
select last_name from actors group by last_name having count(last_name)>1;
#6Q
select actor_name from films_data group by actor_name having count(actor_name)>2;
#7Q
select * from films_data where film_name = 'Academy Dinosaur';
#8Q
insert into films_data value (1007,'Academy Dinosaur', 'Mike Hillyer',180,5000,'family drama');
#9Q
select film_name, min(due) from films_data group by film_name having film_name = 'Academy dinosaur';
#10Q
select  avg(length) from films_data;
#11Q
select category, avg(length) from films_data group by category;