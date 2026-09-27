-- =========================================================
-- EMPLOYEE MANAGEMENT SYSTEM
-- DATABASE SCHEMA
-- =========================================================

-- Create database
CREATE DATABASE IF NOT EXISTS employee_management;

-- Select database
USE employee_management;


-- =========================================================
-- EMPLOYEES TABLE
-- =========================================================

CREATE TABLE IF NOT EXISTS employees (

    employee_id INT PRIMARY KEY AUTO_INCREMENT,

    name VARCHAR(100) NOT NULL,

    email VARCHAR(100) UNIQUE NOT NULL,

    phone VARCHAR(15),

    department VARCHAR(50),

    salary DECIMAL(10,2),

    joining_date DATE

);