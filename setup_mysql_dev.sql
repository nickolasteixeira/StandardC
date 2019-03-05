-- prepares a MySQL server for the project
-- GRANT USAGE ON *.* TO 'dev'@'localhost';
DROP DATABASE dev_db;

CREATE DATABASE IF NOT EXISTS dev_db;

CREATE USER IF NOT EXISTS dev@localhost
	IDENTIFIED BY 'dev_pwd';

USE dev_db;

GRANT ALL PRIVILEGES ON dev_db.*
	TO 'dev'@'localhost';

CREATE TABLE standardc_math
	(id varchar(60) NOT NULL UNIQUE,
     	created_at DATETIME(6) NOT NULL,
       	updated_at DATETIME(6) NOT NULL,
       	a int NOT NULL,
       	b int NOT NULL,
       	c int NOT NULL,
       	d int NOT NULL,
       	x int NOT NULL,
	y1 float NOT NULL,
	y2 float NOT NULL,
	y3 float NOT NULL,	
	PRIMARY KEY (id));

USE performance_schema;

GRANT SELECT ON performance_schema.* TO 'dev'@'localhost';

FLUSH PRIVILEGES;
