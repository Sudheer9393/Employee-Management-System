class Employee:

    def __init__(
        self,
        name,
        email,
        phone,
        department,
        salary,
        joining_date
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.department = department
        self.salary = salary
        self.joining_date = joining_date

    def display_employee(self):

        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Phone: {self.phone}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")
        print(f"Joining Date: {self.joining_date}")

    def __str__(self):

        return (
            f"Employee("
            f"Name={self.name}, "
            f"Email={self.email}, "
            f"Department={self.department}, "
            f"Salary={self.salary}"
            f")"
        )