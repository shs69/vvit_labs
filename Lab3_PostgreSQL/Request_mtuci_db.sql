 create database mtuci_db;

\c mtuci_db 
 
 create table chair (id serial primary key, numb vrachar not null, decanat varchar not null);
 create table student_group(id serial primary key, numb varchar not null references chair(numb), chair_id integer not null);
 create table student(id serial primary key, full_name varchar not null, passport varchar(10) not null, group_id integer not null references student_group(id));

 insert into chair (numb, decanat) values ('Прикладной искуственный интеллект', 'ИТ');
 insert into chair (numb, decanat) values ('Информатика', 'ИТ');

 insert into student_group(numb, chair_id) values ('БВТ2201', '1');
 insert into student_group(numb, chair_id) values ('БВТ2202', '1');
 insert into student_group(numb, chair_id) values ('БИН2201', '2');
 insert into student_group(numb, chair_id) values ('БИН2202', '2');


 insert into student(full_name, passport, group_id) values ('Василий Иванов', '3818101256', '1');
 insert into student(full_name, passport, group_id) values ('Петр Иванченко', '3818113406', '1');
 insert into student(full_name, passport, group_id) values ('Анна Загуляйко', '3818132486', '1');
 insert into student(full_name, passport, group_id) values ('Иннокентий Сыроваров', '3818123456', '1');
 insert into student(full_name, passport, group_id) values ('Ирина Петрова', '3818123456', '1');
 insert into student(full_name, passport, group_id) values ('Григорий Дятлов', '3818123945', '2');
 insert into student(full_name, passport, group_id) values ('Анатолий Горбачев', '3818123358', '2');
 insert into student(full_name, passport, group_id) values ('Василиса Семанченко', '3818043426', '2');
 insert into student(full_name, passport, group_id) values ('Александр Корсаров', '3818195443', '2');
 insert into student(full_name, passport, group_id) values ('Валерия Николаева', '3818192436', '2');
 insert into student(full_name, passport, group_id) values ('Кирилл Заливанов', '3818161646', '3');
 insert into student(full_name, passport, group_id) values ('Артём Якутов', '3818133376', '3');
 insert into student(full_name, passport, group_id) values ('Анастасия Белорусских', '3818133346', '3');
 insert into student(full_name, passport, group_id) values ('София Курчанская', '3818123476', '3');
 insert into student(full_name, passport, group_id) values ('Велимир Загуров', '3818560944','3');
 insert into student(full_name, passport, group_id) values ('Николай Челябский', '3818112226', '4');
 insert into student(full_name, passport, group_id) values ('Иван Каранов', '3818533446', '4');
 insert into student(full_name, passport, group_id) values ('Милена Мирная', '3818431898', '4');
 insert into student(full_name, passport, group_id) values ('Андрей Военных', '3818193555', '4');
 insert into student(full_name, passport, group_id) values ('Алексей Губанов', '3818563399', '4');