# Employee class
class Employee:
    def __init__(self, name, id_number, department, title):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__title = title

    # Return employee name.
    def get_name(self):
        return self.__name

    # Return employee ID number.
    def get_id_number(self):
        return self.__id_number

    # Return department.
    def get_department(self):
        return self.__department

    # Return employee title.
    def get_title(self):
        return self.__title

    # Set employee name.
    def set_name(self, name):
        self.__name = name

    # Set employee ID number.
    def set_id_number(self, id_number):
        self.__id_number = id_number

    # Set department.
    def set_department(self, department):
        self.__department = department

    # Set title.
    def set_title(self, title):
        self.__title = title

    # Prinint employee's name, ID number, department, and title.
    def __str__(self):
        return (f"Name: {self.__name}\nID Number: {self.__id_number}\nDepartment: {self.__department}\nTitle: {self.__title}")