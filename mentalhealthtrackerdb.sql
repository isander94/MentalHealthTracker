use mentalHealthTrackerDB;
create table users (
user_id int auto_increment primary key,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(70) not null,
password varchar(20) not null
);

insert into users
values	(1, "Alex", "Alexsson", "axel@gmail.com", "123"),
		(2, "Oscar", "Alexsson", "axel@gmail.com", "123"),
		(3, "Ala", "Alexsson", "axel@gmail.com", "123");

select * from users;
