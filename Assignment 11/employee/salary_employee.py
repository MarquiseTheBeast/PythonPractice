from employee import Employee

# Salary employee class
class Salary_Employee(Employee):
    def __init__(self, name, employee_type, department, salary):
        Employee.__init__(self, name, employee_type, department, salary)