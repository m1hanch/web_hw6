drop table if exists grades;
drop table if EXISTS subjects;
drop TABLE if EXISTS students;
drop TABLE if exists groups;
drop table if EXISTS teachers;

create table groups(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);


create table students (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(30) not null ,
    date_of_birth date not null ,
    group_id INTEGER NOT NULL,
    foreign key (group_id) references groups(id)
        on delete cascade
        on update cascade
);


create table teachers (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(30) not null
);


create table subjects (
    id SERIAL PRIMARY KEY,
    subject_name VARCHAR(30) not null,
    teacher_id integer not null,
    foreign key (teacher_id) references teachers(id)
                      on delete cascade
                      on update cascade
);


create table grades(
    id serial PRIMARY KEY ,
    student_id integer not null ,
    subject_id integer not null ,
    grade integer check (grade >=0 and grade <=100),
    date_received date not null,
    foreign key (student_id) references students(id)
                   on delete cascade
                   on update cascade,
    foreign key (subject_id) references subjects(id)
                   on delete cascade
                   on update cascade
);


