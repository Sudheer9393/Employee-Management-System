import re
from datetime import datetime

from employee_service import EmployeeService


# =========================================================
# SERVICE OBJECT
# =========================================================

employee_service = EmployeeService()


# =========================================================
# INPUT VALIDATION FUNCTIONS
# =========================================================

def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_integer_input(message):
    while True:
        try:
            value = int(input(message))

            if value <= 0:
                print("Please enter a positive number.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float_input(message):
    while True:
        try:
            value = float(input(message))

            if value < 0:
                print("Salary cannot be negative.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_email_input(message):
    while True:
        email = input(message).strip()

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if re.match(pattern, email):
            return email

        print("Invalid email format. Please enter a valid email.")


def get_phone_input(message):
    while True:
        phone = input(message).strip()

        if phone.isdigit() and len(phone) == 10:
            return phone

        print("Phone number must contain exactly 10 digits.")


def get_date_input(message):
    while True:
        date_input = input(message).strip()

        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD format.")


# =========================================================
# DISPLAY EMPLOYEE
# =========================================================

def display_employee(employee):

    print(f"ID: {employee['employee_id']}")
    print(f"Name: {employee['name']}")
    print(f"Email: {employee['email']}")
    print(f"Phone: {employee['phone']}")
    print(f"Department: {employee['department']}")
    print(f"Salary: {employee['salary']}")
    print(f"Joining Date: {employee['joining_date']}")


# =========================================================
# VIEW ALL EMPLOYEES
# =========================================================

def view_all_employees():

    employees = employee_service.get_all_employees()

    if not employees:
        print("\nNo employees found.")
        return

    print("\n========== Employee List ==========")

    for employee in employees:

        display_employee(employee)

        print("----------------------------------")
        print()


# =========================================================
# SEARCH EMPLOYEE
# =========================================================

def search_employee_by_id():

    employee_id = get_integer_input(
        "Enter Employee ID: "
    )

    employee = employee_service.search_employee(
        employee_id
    )

    if employee:

        print("\n========== Employee Found ==========")

        display_employee(employee)

    else:

        print("Employee not found.")


# =========================================================
# UPDATE EMPLOYEE
# =========================================================

def update_employee_by_id():

    print("\n--- Update Employee ---")

    employee_id = get_integer_input(
        "Enter Employee ID: "
    )

    existing_employee = employee_service.search_employee(
        employee_id
    )

    if existing_employee:

        print("\nCurrent Employee Details:")

        display_employee(existing_employee)

        print("\nEnter New Details:")

        name = get_non_empty_input(
            "Enter New Name: "
        )

        email = get_email_input(
            "Enter New Email: "
        )

        phone = get_phone_input(
            "Enter New Phone: "
        )

        department = get_non_empty_input(
            "Enter New Department: "
        )

        salary = get_float_input(
            "Enter New Salary: "
        )

        joining_date = get_date_input(
            "Enter New Joining Date (YYYY-MM-DD): "
        )

        employee_service.update_employee(
            employee_id,
            name,
            email,
            phone,
            department,
            salary,
            joining_date
        )

    else:

        print("Employee not found.")


# =========================================================
# DELETE EMPLOYEE
# =========================================================

def delete_employee_by_id():

    print("\n--- Delete Employee ---")

    employee_id = get_integer_input(
        "Enter Employee ID: "
    )

    existing_employee = employee_service.search_employee(
        employee_id
    )

    if existing_employee:

        print("\nEmployee Details:")

        display_employee(existing_employee)

        confirmation = input(
            "\nAre you sure you want to delete this employee? (yes/no): "
        ).strip().lower()

        if confirmation == "yes":

            employee_service.delete_employee(
                employee_id
            )

        elif confirmation == "no":

            print("Delete operation cancelled.")

        else:

            print(
                "Invalid choice. Delete operation cancelled."
            )

    else:

        print("Employee not found.")


# =========================================================
# ADD EMPLOYEE
# =========================================================

def add_new_employee():

    print("\n--- Add Employee ---")

    name = get_non_empty_input(
        "Enter Name: "
    )

    email = get_email_input(
        "Enter Email: "
    )

    phone = get_phone_input(
        "Enter Phone: "
    )

    department = get_non_empty_input(
        "Enter Department: "
    )

    salary = get_float_input(
        "Enter Salary: "
    )

    joining_date = get_date_input(
        "Enter Joining Date (YYYY-MM-DD): "
    )

    employee_service.add_employee(
        name,
        email,
        phone,
        department,
        salary,
        joining_date
    )


# =========================================================
# MAIN MENU
# =========================================================

def main():

    while True:

        print("\n================================")
        print("     EMPLOYEE MANAGEMENT SYSTEM")
        print("================================")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("================================")

        choice = input(
            "Enter your choice: "
        ).strip()

        # -------------------------------------------------
        # ADD EMPLOYEE
        # -------------------------------------------------

        if choice == "1":

            add_new_employee()

        # -------------------------------------------------
        # VIEW ALL EMPLOYEES
        # -------------------------------------------------

        elif choice == "2":

            view_all_employees()

        # -------------------------------------------------
        # SEARCH EMPLOYEE
        # -------------------------------------------------

        elif choice == "3":

            search_employee_by_id()

        # -------------------------------------------------
        # UPDATE EMPLOYEE
        # -------------------------------------------------

        elif choice == "4":

            update_employee_by_id()

        # -------------------------------------------------
        # DELETE EMPLOYEE
        # -------------------------------------------------

        elif choice == "5":

            delete_employee_by_id()

        # -------------------------------------------------
        # EXIT
        # -------------------------------------------------

        elif choice == "6":

            print(
                "\nThank you for using Employee Management System."
            )

            break

        # -------------------------------------------------
        # INVALID OPTION
        # -------------------------------------------------

        else:

            print(
                "\nInvalid choice. Please enter a number "
                "between 1 and 6."
            )


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()