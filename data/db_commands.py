
'''

create table authors (
id SERIAL primary key,
first_name VARCHAR(255),
last_name VARCHAR(255)
);


insert into authors(first_name, last_name) values('Jan', 'Kowalski');
insert into authors(first_name, last_name) values('Janusz', 'Mielnik');

select * from authors;

'''