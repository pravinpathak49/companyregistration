CREATE DATABASE company_db;

USE company_db;

CREATE TABLE company (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    business_type VARCHAR(255) NOT NULL,
    business_location VARCHAR(255) NOT NULL
);
