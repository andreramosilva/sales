CREATE DATABASE db_sales;

 use db_sales;

CREATE TABLE sales (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
product VARCHAR(30) NOT NULL,
seller_id VARCHAR(30) NOT NULL,
costumer_name VARCHAR(30) NOT NULL,
sale_value float NOT NULL,
date_sale TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE seller (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(30) NOT NULL,
reg_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

--sellers
INSERT INTO seller (name)
VALUES ('xpto');

INSERT INTO seller (name)
VALUES ('seller2');

INSERT INTO seller (name)
VALUES ('magazine');

INSERT INTO seller (name)
VALUES ('magaloca');

INSERT INTO user_amigo (nome, nome_amigo)
VALUES ('carlos');