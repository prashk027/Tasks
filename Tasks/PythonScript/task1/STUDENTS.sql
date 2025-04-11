CREATE TABLE
    STUDENTS (
        ID Serial PRIMARY key,
        FIRST_NAME VARCHAR(255) DEFAULT NULL,
        LAST_NAME VARCHAR(255) DEFAULT NULL,
        AGE INT CHECK (AGE < 100),
        EMAIL VARCHAR(255) DEFAULT NULL,
        PHONE VARCHAR(13) DEFAULT NULL
    );

create table
    stud (id serial not null, name varchar(200));

insert into stud('peter');