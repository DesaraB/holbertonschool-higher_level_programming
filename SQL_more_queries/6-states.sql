-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id int UNIQUE AUTO_INCREMENT NOT NULL,
	name varchar(256) NOT NULL,
	PRIMARY KEY (ID)
);
