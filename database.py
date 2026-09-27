import os

import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# DATABASE CONNECTION
# =========================================================

def create_connection():

    try:

        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )

        return connection

    except Error as error:

        print(f"Database connection error: {error}")
        return None


# =========================================================
# ADD EMPLOYEE
# =========================================================

def add_employee(employee):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            INSERT INTO employees
            (name, email, phone, department, salary, joining_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            employee.name,
            employee.email,
            employee.phone,
            employee.department,
            employee.salary,
            employee.joining_date
        )

        cursor.execute(query, values)

        connection.commit()

        print("Employee added successfully.")

    except Error as error:

        connection.rollback()

        if error.errno == 1062:
            print("Error: Email already exists.")

        else:
            print(f"Database error: {error}")

    finally:

        if cursor is not None:
            cursor.close()

        connection.close()


# =========================================================
# GET ALL EMPLOYEES
# =========================================================

def get_all_employees():

    connection = create_connection()

    if connection is None:
        return []

    cursor = None

    try:

        cursor = connection.cursor(dictionary=True)

        query = "SELECT * FROM employees"

        cursor.execute(query)

        employees = cursor.fetchall()

        return employees

    except Error as error:

        print(f"Database error: {error}")
        return []

    finally:

        if cursor is not None:
            cursor.close()

        connection.close()


# =========================================================
# SEARCH EMPLOYEE
# =========================================================

def search_employee(employee_id):

    connection = create_connection()

    if connection is None:
        return None

    cursor = None

    try:

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT * FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        employee = cursor.fetchone()

        return employee

    except Error as error:

        print(f"Database error: {error}")
        return None

    finally:

        if cursor is not None:
            cursor.close()

        connection.close()


# =========================================================
# UPDATE EMPLOYEE
# =========================================================

def update_employee(
    employee_id,
    name,
    email,
    phone,
    department,
    salary,
    joining_date
):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            UPDATE employees
            SET name = %s,
                email = %s,
                phone = %s,
                department = %s,
                salary = %s,
                joining_date = %s
            WHERE employee_id = %s
        """

        values = (
            name,
            email,
            phone,
            department,
            salary,
            joining_date,
            employee_id
        )

        cursor.execute(query, values)

        connection.commit()

        if cursor.rowcount > 0:
            print("Employee updated successfully.")

        else:
            print("Employee not found.")

    except Error as error:

        connection.rollback()

        if error.errno == 1062:
            print("Error: Email already exists.")

        else:
            print(f"Database error: {error}")

    finally:

        if cursor is not None:
            cursor.close()

        connection.close()


# =========================================================
# DELETE EMPLOYEE
# =========================================================

def delete_employee(employee_id):

    connection = create_connection()

    if connection is None:
        return

    cursor = None

    try:

        cursor = connection.cursor()

        query = """
            DELETE FROM employees
            WHERE employee_id = %s
        """

        cursor.execute(query, (employee_id,))

        connection.commit()

        if cursor.rowcount > 0:
            print("Employee deleted successfully.")

        else:
            print("Employee not found.")

    except Error as error:

        connection.rollback()

        print(f"Database error: {error}")

    finally:

        if cursor is not None:
            cursor.close()

        connection.close()