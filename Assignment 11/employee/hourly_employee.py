from employee import Employee

# Hourly employee class
class Hourly_Employee(Employee):
    def __init__(self, name, employee_type, department, salary):
        Employee.__init__(self, name, employee_type, department, salary)