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
SELECT note, date_now from notes where user_id = 4;

create table mood_ratings (
mood_rating_id int auto_increment primary key not null,
mood_rating int not null,
user_id int,
date_now datetime default current_timestamp,
foreign key (user_id) references users(user_id)
);
select * from mood_ratings;
select mood_rating from mood_ratings where user_id = 4;
insert into mood_ratings (mood_rating, user_id, date_now) values (5, 4, "2024-05-18"),
																 (6, 4, "2024-05-19"),
																 (7, 4, "2024-05-20"),
																 (8, 4, "2024-05-21"),
																 (9, 4, "2024-05-23"),
																 (10, 4, "2024-05-24"),
																 (5, 4, "2024-05-25");