import os
import pickle
from employee import Employee

# Constant variables.
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
EXIT = 5

# Read/write employee.dat in the same folder.
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILENAME = os.path.join(SCRIPT_DIR, 'employee.dat')

# Display menu of choices.
def display_menu():
    print("\nMenu\n============================================")
    print("1. Look up an employee\n2. Add a new employee\n3. Change an existing employee\n4. Delete an employee\n5. Exit the program")

# Load employees from file.
def load_employees():
    # Used to store dictionary contents from the .dat file.
    employee_contents = {}

    # Open file and unpickle the objects, storing all contents inside the dictionary. 
    with open(FILENAME, 'rb') as file:
        employee_contents = pickle.load(file)

    return employee_contents

# Look up an employee in the list.
def look_up_employee(employees):
    try:
        # Entering employee ID number.
        id_number_input = input("Enter an employee ID number: ")

        found = False
        for emp in employees:
            if id_number_input == emp.get_id_number():
                print(f"Name: {emp.get_name()}\nID: {emp.get_id_number()}\nDepartment: {emp.get_department()}\nTitle: {emp.get_title()}")
                found = True
                break

        if not found:
            print("The specified ID number was not found.")
    except:
        print("Invalid input.")

# This function adds an employee to the list.
def add_employee(employees):
    # Entering new employee's name, id number, department, and title.
    name_input = input("Enter new employee name: ")
    id_number_input = input("Enter new employee ID number: ")
    department_input = input("Enter new employee department: ")
    title_input = input("Enter new employee title: ")

    # Check to make sure ID number input doesn't already exist.
    does_id_exist = False
    for emp in employees:
        if id_number_input == emp.get_id_number():
            does_id_exist = True
            
    # If ID number input doesn't exists, then add new employee.
    if not does_id_exist:
        new_employee = Employee(name_input, id_number_input, department_input, title_input)
        employees.append(new_employee)
        print("The new employee has been added.")
    else:
        print("Unable to add new employee. The ID number already exists in the system.")

# This function changes an existing employee's information.
def change_employee(employees):
    # Entering employee ID number.
    id_number_input = input("Enter employee ID number: ")

    # Check if the ID number exists in the list.
    is_found = False
    for emp in employees:
        if id_number_input == emp.get_id_number():
            # Entering the new name, new department, and new title for the employee.
            new_name = input("Enter the new name: ")
            new_department = input("Enter the new department: ")
            new_title = input("Enter the new title: ")

            # Updating the name, department, and title in employee's class.
            emp.set_name(new_name)
            emp.set_department(new_department)
            emp.set_title(new_title)
            print("Employee information updated.")

            is_found = True
            break

    if not is_found:
        print("The specified ID number was not found.")

# This function removes an employee from the list.
def delete_employee(employees):
    # Entering employee ID number.
    id_number_input = input("Enter employee ID number: ")

    # If ID number exists, remove employee from list.
    is_found = False
    for emp in employees:
        if id_number_input == emp.get_id_number():
            employees.remove(emp)
            is_found = True
            print("Employee information deleted.")
            break

    if not is_found:
        print("The specified ID number was not found.")

# Save employee list information to file.
def save_employees(employees):
    # Open file and pickle the dictionary contents to the file.
    with open(FILENAME, 'wb') as output_file:
        pickle.dump(employees, output_file)
        print("Information saved to file.")

def main():
    # Load contents from file.
    employees_list = load_employees()

    # Loop until user exits.
    is_finished = False
    while not is_finished:
        try:
            # Display selection menu.
            display_menu()

            # Prompted to enter a selection choice.
            input_selection = int(input("\nEnter your choice: "))
    
            if input_selection == LOOK_UP:
                look_up_employee(employees_list)
            elif input_selection == ADD:
                add_employee(employees_list)
            elif input_selection == CHANGE:
                change_employee(employees_list)
            elif input_selection == DELETE:
                delete_employee(employees_list)
            elif input_selection == EXIT:
                # Once finished, save employees list to .dat file.
                is_finished = True
                save_employees(employees_list)
            else:
                print("Error: Selection must be 1, 2, 3, 4, or 5.")
        except ValueError:
            print("Invalid input. Please try again. Input must be an integer with selection of 1, 2, 3, 4, or 5.")

if __name__ == '__main__':
    main()