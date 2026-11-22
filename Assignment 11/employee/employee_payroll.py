# TODO: import your own Employee superclass and subclasses here, e.g.:
from hourly_employee import Hourly_Employee
from commission_employee import Commission_Employee
from salary_employee import Salary_Employee
from employee import Employee

# Constant employee types as strings.
HOURLY_EMPLOYEE_STR = 'Hourly Employee'
SALARIED_EMPLOYEE_STR = 'Salaried Employee'
COMMISSION_EMPLOYEE_STR = 'Commission Employee'
EMPLOYEE_STR = 'Employee'

def load_employees():
    # Employees list.
    employees = []

    # Employee dictionary with hardcoded employee names as the keys and the values being a list containing the type of employee, department, and salary.
    # A list containing commission employee will have a base pay value (in last element of that list) that will be used to calculate the commission.
    employees_dict = {
        'Nick DeFalco': [HOURLY_EMPLOYEE_STR, 'Sales', 52000],
        'Applejack Johnson': [SALARIED_EMPLOYEE_STR, 'Sales', 44000],
        'Mario Dubois': [SALARIED_EMPLOYEE_STR, 'Sales', 77200],
        'Anthony Jo': [SALARIED_EMPLOYEE_STR, 'Engineering', 98000],
        'Stephanie Johnson': [EMPLOYEE_STR, 'Engineering', 31200],
        'Dominic Togo': [COMMISSION_EMPLOYEE_STR, 'Maintenance', 65000, 20000],
        'Christina Gonzalez': [HOURLY_EMPLOYEE_STR, 'Maintenance', 41184],
        'Geoffrey Dav': [HOURLY_EMPLOYEE_STR, 'HR', 135200]
        }

    # Loop through each dictionary key. 
    for emp in employees_dict.keys():
        # Assign name.
        employee_name = emp

        # Assign type of employee.
        employee_type = employees_dict[emp][0]

        # Assign department.
        department = employees_dict[emp][1]

        # Assign salary.
        salary = employees_dict[emp][-1] if employees_dict[emp][0] != COMMISSION_EMPLOYEE_STR else employees_dict[emp][-2] # Useful if employee is/isn't commission emplyee

        # Check the type of employee.
        if employee_type == HOURLY_EMPLOYEE_STR:
            # Create new hourly employee.
            new_hourly_employee = Hourly_Employee(employee_name, employee_type, department, salary)
            employees.append(new_hourly_employee)
        elif employee_type == SALARIED_EMPLOYEE_STR:
            # Create new salaried employee.
            new_salary_employee = Salary_Employee(employee_name, employee_type, department, salary)
            employees.append(new_salary_employee)
        elif employee_type == COMMISSION_EMPLOYEE_STR:
            # Create new commission employee with added base pay that will be used for calculating commission value.
            base_pay = employees_dict[emp][-1]
            new_commission_employee = Commission_Employee(employee_name, employee_type, department, salary, base_pay)
            employees.append(new_commission_employee)
        elif employee_type == EMPLOYEE_STR:
            # Create new hourly employee.
            new_hourly_employee = Hourly_Employee(employee_name, employee_type, department, salary)
            employees.append(new_hourly_employee)

    # Return employee list.
    return employees


def main():
    employees = load_employees()
    employee_dict = {}

    # Create dictionary department keys with no duplicated keys and setting the value as an empty list.
    for emp in employees:
        employee_dict[emp.get_department()] = []

    # Storing each employee in the value's list.
    for emp in employees:
        employee_dict[emp.get_department()].append(emp)

    # Loop through each department and list contained in the department key.
    for department, emp_list in employee_dict.items():
        # Total payroll used for each department. Resets to 0 on each loop.
        total_payroll = 0

        # Print each department that includes each employee's name, employee type, and salary.
        print(f"Department: {department}")
        for emp in emp_list:
            print(f"    {emp.get_name()} ({emp.get_employee_type()}): ${emp.get_salary():.2f}")

            # Print commission breakdown if employee is a commission employee. 
            if emp.get_employee_type() == COMMISSION_EMPLOYEE_STR:
                print(emp.commission_breakdown())

            # Add employee's salary to total payroll.
            total_payroll += emp.get_salary()

        # Printing total payroll.
        print(f"Total Payroll: ${total_payroll:.2f}\n")


if __name__ == "__main__":
    main()
