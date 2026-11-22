# Employee class
class Employee:
    def __init__(self, name, employee_type, department, salary):
        self.__name = name
        self.__employee_type = employee_type
        self.__department = department
        self.__salary = salary

    # Set name.
    def set_name(self, name):
        self.__name = name

    # Set the type of employee.
    def set_employee_type(self, employee_type):
        self.__employee_type = employee_type

    # Set department.
    def set_department(self, department):
        self.__department = department

    # Set salary.
    def set_salary(self, salary):
        self.__salary = salary

    # Return name.
    def get_name(self):
        return self.__name

    # Return the type of employee.
    def get_employee_type(self):
        return self.__employee_type

    # Return department.
    def get_department(self):
        return self.__department

    # Return salary.
    def get_salary(self):
        return self.__salary