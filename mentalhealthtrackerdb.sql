use mentalHealthTrackerdb;
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


use mentalHealthTrackerdb;
create table notes (
note_id int auto_increment primary key not null,
note varchar(200) not null,
user_id int,
date_now datetime default current_timestamp,
foreign key (user_id) references users(user_id)
);

select * from notes;
SELECT note and date_now from notes where user_id = 4;
drop table notes;
insert into notes (note, user_id) values ("HIHI", 2),
					 ("NAAA", 3);
