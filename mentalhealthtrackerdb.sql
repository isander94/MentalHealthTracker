use mentalHealthTrackerDB;
create table users (
user_id int,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(70) not null
);

insert into users
values	(1, "Alex", "Alexsson", "axel@gmail.com"),
		(2, "Oscar", "Alexsson", "axel@gmail.com"),
		(3, "Ala", "Alexsson", "axel@gmail.com");

select * from users;
