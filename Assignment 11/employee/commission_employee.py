from employee import Employee

# Commission Employee class
class Commission_Employee(Employee):
    def __init__(self, name, employee_type, department, salary, base_pay):
        Employee.__init__(self, name, employee_type, department, salary)
        self.__base_pay = base_pay

    # Commission breakdown with percentage of earnings.
    def commission_breakdown(self):
        # Calculate commission value.
        commission = self.get_salary() - self.__base_pay

        # Calculate earnings value.
        earnings = (commission / self.get_salary()) * 100

        # Print string containing base pay, commission, and percentage of earnings. 
        # {"":<8} is used for left alignment by 8.
        print(f"{"":<8}Base ${self.__base_pay:.2f} + Commission ${commission:.2f} ({earnings:.1f}% of earnings)")