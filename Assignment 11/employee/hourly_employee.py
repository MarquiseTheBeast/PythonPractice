from employee import Employee

# Hourly Employee class
class Hourly_Employee(Employee):
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)