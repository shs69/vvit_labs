-- Заполнение таблицы subject

insert into subject values ('Введение в информационные технологии (Лаб.Занятие)');
insert into subject values ('Введение в информационные технологии (Практика)');
insert into subject values ('Математические основы баз данных (Лекция)');
insert into subject values ('Математические основы баз данных (Практика)');
insert into subject values ('Математические основы баз данных (Лаб.Занятие)');
insert into subject values ('Основы DevOps (Лекция)');
insert into subject values ('Основы DevOps (Практика)');
insert into subject values ('Основы DevOps (Лаб.Занятие)');
insert into subject values ('Выcшая математика (Лекция)');
insert into subject values ('Высшая математика (Практика)');
insert into subject values ('Физика (Лекция)');
insert into subject values ('Физика (Лаб.Занятие)');
insert into subject values ('Физика (Практика)');
insert into subject values ('Проектный практикум (Практика)');
insert into subject values ('История (Лекция)');
insert into subject values ('История (Практика)');
insert into subject values ('Игровые виды спорта (Практика)');
insert into subject values ('Иностранный язык (Практика)');

-- Заполнение таблицы teacher

insert into teacher values (1, 'Вальковский С.Н.', 'Физика (Лекция)');
insert into teacher values (2, 'Волохова С.В.', 'Игровые виды спорта (Практика)');
insert into teacher values (3, 'Воронова Е.В.', 'Иностранный язык (Практика)');
insert into teacher values (4, 'Городничев М.Г.', 'Основы DevOps (Лекция)');
insert into teacher values (5, 'Изотова А.А.', 'Математические основы баз данных (Лаб.Занятие)');
insert into teacher values (6, 'Липатов В.Н.', 'Основы DevOps (Практика)');
insert into teacher values (7, 'Липатов В.Н.', 'Основы DevOps (Лаб.Занятие)');
insert into teacher values (8, 'Полищук Ю.В.', 'Математические основы баз данных (Лекция)');
insert into teacher values (9, 'Полищук Ю.В.', 'Математические основы баз данных (Практика)');
insert into teacher values (10, 'Потапченко Т.Д.', 'Проектный практикум (Практика)');
insert into teacher values (11, 'Скляр Л.Н.', 'История (Практика)');
insert into teacher values (12, 'Скляр Л.Н.', 'История (Лекция)');
insert into teacher values (13, 'Тренин А.Е.', 'Физика (Лаб.Занятие)');
insert into teacher values (14, 'Файзулаев В.Н.', 'Физика (Практика)');
insert into teacher values (15, 'Фурлетов Ю.М.', 'Введение в информационные технологии (Лаб.Занятие)');
insert into teacher values (16, 'Фурлетов Ю.М.', 'Введение в информационные технологии (Практика)');
insert into teacher values (17, 'Шаймарданова Л.К.', 'Выcшая математика (Лекция)');
insert into teacher values (18, 'Шаймарданова Л.К.', 'Высшая математика (Практика)');

-- Заполнение таблицы timetable
-- ВСЕ ЗАТУПКИ, ВНИМАНИЕ!!! ПЕРВЫЕ 7 ДНЕЙ - ЧЁТНАЯ(НИЖНЯЯ) НЕДЕЛЯ, ВТОРЫЕ 7 ДНЕЙ - НЕЧЁТНАЯ(ВЕРХНЯЯ) НЕДЕЛЯ!!!!!!
insert into timetable values (1, 'Пн', 'Высшая математика (Лекция)', '514', '11:20', 'чётная');
insert into timetable values (2, 'Пн', 'История (Практика)', '316', '13:10', 'чётная');
insert into timetable values (3, 'Пн', 'Физика (Лаб.Занятие)', '340', '15:25', 'чётная');
insert into timetable values (4, 'Пн', 'Математические основы баз данных (Лаб.Занятие)', '519', '17:15', 'чётная');
insert into timetable values (5, 'Ср', 'Проектный практикум (Практика)', '208', '9:30', 'чётная');
insert into timetable values (6, 'Ср', 'Основы DevOps (Лаб.Занятие)', '302', '11:20', 'чётная');
insert into timetable values (7, 'Ср', 'Основы DevOps (Лекция)', '414', '13:10', 'чётная');
insert into timetable values (8, 'Чт', 'Введение в информационные технологии (Лаб.Занятие)', '205', '9:30', 'чётная');
insert into timetable values (9, 'Чт', 'Введение в информационные технологии (Практика)', '205', '11:20', 'чётная');
insert into timetable values (10, 'Пт', 'Высшая математика (Практика)', '330', '11:20', 'чётная');
insert into timetable values (11, 'Пт', 'Игровые виды спорта (Практика)', '3', '13:10', 'чётная');
insert into timetable values (12, 'Пн', 'Игровые виды спорта (Практика)', '3', '9:30', 'нечётная');
insert into timetable values (13, 'Пн', 'Иностранный язык (Практика)', '322', '11:20', 'нечётная');
insert into timetable values (14, 'Вт', 'Иностранный язык (Практика)', '405', '11:20', 'нечётная');
insert into timetable values (15, 'Вт', 'Физика (Практика)', '332', '13:10', 'нечётная');
insert into timetable values (16, 'Вт', 'История (Практика)', '404', '15:25', 'нечётная');
insert into timetable values (17, 'Ср', 'Высшая математика (Практика)', '301', '11:20', 'нечётная');
insert into timetable values (18, 'Ср', 'Выcшая математика (Лекция)', '514', '13:10', 'нечётная');
insert into timetable values (19, 'СР', 'Физика (Лекция)', '226', '15:25', 'нечётная');
insert into timetable values (20, 'Чт', 'Введение в информационные технологии (Лаб.Занятие)', '203', '9:30', 'нечётная');
insert into timetable values (21, 'Чт', 'Основы DevOps (Лаб.Занятие)', '206', '11:20', 'нечётная');
insert into timetable values (22, 'Пт', 'История (Лекция)', '227', '9:30', 'нечётная');
insert into timetable values (23, 'Пт', 'Математические основы баз данных (Лекция)', '535', '11:20', 'нечётная');
insert into timetable values (24, 'Пт', 'Игровые виды спорта (Практика)', '3', '13:10', 'нечётная');
insert into timetable values (25, 'Пт', 'Математические основы баз данных (Практика)', '410', '15:25', 'нечётная');