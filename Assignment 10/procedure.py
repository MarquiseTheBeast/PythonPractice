# Procedure class
class Procedure:
    def __init__(self, procedure, date, practitioner, charge_value):
        self.__procedure = procedure
        self.__date = date
        self.__practitioner = practitioner
        self.__charge_value = charge_value

    # Return procedure.
    def get_procedure(self):
        return self.__procedure

    # Return date.
    def get_date(self):
        return self.__date

    # Return practitioner.
    def get_practitioner(self):
        return self.__practitioner

    # Return charge value.
    def get_charge_value(self):
        return self.__charge_value

    # Set procedure.
    def set_procedure(self, procedure):
        self.__procedure = procedure

    # Set date.
    def set_date(self, date):
        self.__date = date

    # Set practitioner.
    def set_practitioner(self, practitioner):
        self.__practitioner = practitioner

    # Set charge value.
    def set_charge_value(self, charge_value):
        self.__charge_value = charge_value

    def __str__(self):
        return (f"Procedure: {self.__procedure}\nDate: {self.__date}\nPractitioner: {self.__practitioner}\nCharge: {self.__charge_value:.2f}")