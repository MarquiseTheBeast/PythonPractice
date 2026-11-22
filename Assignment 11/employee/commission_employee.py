from employee import Employee

# Commission Employee class
class Commission_Employee(Employee):
    def __init__(self, name, employee_type, department, salary, base_pay):
        Employee.__init__(self, name, employee_type, department, salary)
        self.__base_pay = base_pay

    # Set base pay.
    def set_base_pay(self, base_pay):
        self.__base_pay = base_pay

    # Return base pay.
    def get_base_pay(self):
        return self.__base_pay

    # Commission breakdown with percentage of earnings.
    def commission_breakdown(self):
        commission = self.get_salary() - self.__base_pay
        earnings = (commission / self.get_salary()) * 100
        print(f"\tBase ${self.__base_pay:.2f} + Commission ${commission:.2f} ({earnings:.1f}% of earnings)")