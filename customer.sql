-- SELECT * FROM mydata.customer; 
CREATE DATABASE IF NOT EXISTS mydata;

USE mydata;

CREATE TABLE IF NOT EXISTS customer (
    ref VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100),
    mother VARCHAR(100),
    gender VARCHAR(10),
    post VARCHAR(20),
    mobile VARCHAR(15),
    email VARCHAR(100),
    nationality VARCHAR(50),
    idproof VARCHAR(50),
    idnumber VARCHAR(50),
    address VARCHAR(255)
);
