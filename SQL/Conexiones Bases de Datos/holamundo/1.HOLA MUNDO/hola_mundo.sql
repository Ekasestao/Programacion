create database holamundo; -- PARA CREAR UNA BASE DE DATOS
show databases; -- PARA VER LAS BASES DE DATOS
use holamundo; -- PARA USAR LA BASE DE DATOS
-- drop table animales; PARA BORRAR UNA TABLA

-- CREAR UNA TABLA
CREATE TABLE `animales` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tipo` varchar(255) DEFAULT NULL,
  `estado` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

insert into animales (tipo, estado) values ('chanchito','feliz');
insert into animales (tipo, estado) values ('dragon','feliz');
insert into animales (tipo, estado) values ('felipe','triste');

select * from animales;
select * from animales where id = 1;
select * from animales where estado = 'feliz' and tipo = 'chanchito';

update animales set estado = 'feliz' where id = 3; -- MODIFICAR EL VALOR DE UNA COLUMNA

delete from animales where id = 3;

update animales set estado = 'triste' where id = 2;