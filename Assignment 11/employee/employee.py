# Employee class
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary