use mentalHealthTrackerDB;
create table users (
user_id int auto_increment primary key not null,
first_name varchar(50) not null,
last_name varchar(50) not null,
email varchar(70) not null,
password varchar(20) not null
);

insert into users (first_name, last_name, email, password)
values	("Alex", "Alexsson", "axel@gmail.com", "123"),
		("Oscar", "Alexsson", "axel@gmail.com", "123"),
		("Ala", "Alexsson", "axel@gmail.com", "123");

select * from users;
