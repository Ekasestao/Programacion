use holamundo;

create table user (
	id int not null auto_increment,
    name varchar (50) not null,
    edad int not null,
    email varchar (100) not null,
    primary key (id)
    );
    
insert into user (name, edad, email) values ('Ekaitz', 20, 'ekaitzcampo2002@gmail.com');
insert into user (name, edad, email) values ('Oscar', 25, 'oscar@gmail.com');
insert into user (name, edad, email) values ('Layla', 15, 'layla@gmail.com');
insert into user (name, edad, email) values ('Chanchito', 36, 'chanchito@gmail.com');

select * from user;
select * from user limit 1;
select * from user where edad > 15;
select * from user where edad >=15;
select * from user where edad >= 20 and email = 'ekaitzcampo2002@gmail.com';
select * from user where edad >= 20 or email = 'chanchito@gmail.com';
select * from user where email != 'chanchito@gmail.com';
select * from user where edad between 15 and 30;
select * from user where email like '%gmail%';
select * from user where email like '%gmail';
select * from user where email like 'ekaitz%';

select * from user order by edad asc;
select * from user order by edad desc;

select max(edad) as mayor from user;
select min(edad) as menor from user;

select id, name from user;
select id, name as nombre from user;