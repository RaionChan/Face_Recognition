-- Run this SQL code for making this project database's, please make sure you have already have MySQL installed on your computer

create database face_recognizer;

USE face_recognizer;

CREATE TABLE student (
    student_id INT(10) AUTO_INCREMENT PRIMARY KEY NOT NULL,
    dep VARCHAR(20) NULL,
    course VARCHAR(20) NULL,
    year VARCHAR(10) NULL,
    semester VARCHAR(3),
    name VARCHAR(30) NULL,
    division VARCHAR(20) NULL,
    npm VARCHAR(15) NULL,
    gender VARCHAR(10) NULL,
    DOB VARCHAR(11) NULL,
    email VARCHAR(50) NULL,
    phone VARCHAR(15) NULL,
    address VARCHAR(100) NULL,
    teacher VARCHAR(30) NULL,
);

--Then ur database is set and ready to use