from employee import Employee
from database import (
    add_employee,
    get_all_employees,
    search_employee,
    update_employee,
    delete_employee
)


class EmployeeService:

    def add_employee(
        self,
        name,
        email,
        phone,
        department,
        salary,
        joining_date
    ):
        employee = Employee(
            name,
            email,
            phone,
            department,
            salary,
            joining_date
        )

        return add_employee(employee)

    def get_all_employees(self):
        return get_all_employees()

    def search_employee(self, employee_id):
        return search_employee(employee_id)

    def update_employee(
        self,
        employee_id,
        name,
        email,
        phone,
        department,
        salary,
        joining_date
    ):
        return update_employee(
            employee_id,
            name,
            email,
            phone,
            department,
            salary,
            joining_date
        )

    def delete_employee(self, employee_id):
        return delete_employee(employee_id)