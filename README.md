# Employee Management System

A Python and MySQL based Employee Management System that provides
CRUD operations for managing employee information through a
command-line interface.

## Project Overview

The Employee Management System is a backend-oriented application
developed using Python, Object-Oriented Programming, and MySQL.

The application allows users to:

- Add employees
- View all employees
- Search employees by ID
- Update employee information
- Delete employees
- Validate user input
- Handle database errors
- Prevent duplicate email addresses

The project follows a simple layered architecture to separate
application logic from database operations.

---

## Features

### 1. Add Employee

Users can add an employee by providing:

- Name
- Email
- Phone number
- Department
- Salary
- Joining date

### 2. View All Employees

Displays all employees stored in the MySQL database.

### 3. Search Employee

Searches for an employee using the employee ID.

### 4. Update Employee

Allows existing employee information to be modified.

### 5. Delete Employee

Allows an employee record to be deleted after confirmation.

### 6. Input Validation

The application validates:

- Empty inputs
- Email format
- Phone number
- Salary
- Employee ID
- Joining date

### 7. Database Error Handling

The application handles common database errors and
rolls back transactions when required.

### 8. Duplicate Email Handling

Email addresses are stored as unique values in the database,
preventing duplicate employee records.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| MySQL | Database |
| mysql-connector-python | Python-MySQL connectivity |
| python-dotenv | Environment variable management |
| SQL | Database operations |
| Git | Version control |
| GitHub | Source code hosting |

---

## Project Architecture

The project follows a simple layered structure:

```text
User
  |
  v
main.py
  |
  v
EmployeeService
  |
  v
database.py
  |
  v
MySQL Database
