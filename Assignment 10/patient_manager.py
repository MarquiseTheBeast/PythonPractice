from patient import Patient
from procedure import Procedure


def create_patient():
    """Prompt for name, address, and phone, and return a new Patient."""

    first_name = input("Enter first name: ")
    middle_name = input("Enter middle name: ")
    last_name = input("Enter last name: ")
    address = input("Enter address: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    zip_code = input("Enter ZIP code: ")
    phone_number = input("Enter phone number: ")
    emergency_contact = input("Enter emergency contact: ")
    emergency_phone_number = input("Enter emergency phone number: ")

    # Assign patient class to variable and return it.
    new_patient = Patient(first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact, emergency_phone_number)
    return new_patient

def create_procedure():
    """Prompt for procedure details and return a new Procedure.

    The charge must be validated: keep re-prompting until the user
    enters a number greater than 0.
    """

    # Enter procedure, date, and practitioner.
    procedure = input("Enter procedure: ")
    date = input("Enter date: ")
    practitioner = input("Enter Practitioner: ")

    # Loop until charge value is valid.
    is_valid = False
    while not is_valid:
        try:
            # Prompt to enter charge value.
            charge_value_input = float(input("Enter charge value: "))

            # If charge value is 0 or less, user is prompted to enter value again until valid.
            if charge_value_input <= 0:
                print("Error: Charge value must be greater than 0.")
            else:
                is_valid = True
        except ValueError:
            print("Invalid input. Please try again. Charge value must be greater than 0.")

    # Create new procedure and return it.
    new_procedure = Procedure(procedure, date, practitioner, charge_value_input)
    return new_procedure


def main():
    patient = create_patient()

    procedures = []
    # print("\nAdd one or more procedures (enter 'n' to stop).")
    # TODO - create a loop to allow a user adding 0 to multiple procedures for the patient
    #        use create_procedure() to instantiate each procedure object

    # Loop until finished.
    is_finished = False
    while not is_finished:
        # Enter input choosing to add procedure or to stop.
        input_string = input("Add procedure? (0 to add, enter 'n' to stop): ")
        
        if input_string == '0': 
            # Create new procedure and add to list.
            new_procedure = create_procedure()
            procedures.append(new_procedure)
        elif input_string == 'n':
            is_finished = True  
        else: 
            print("Error: Try again. Either type '0' to add procedure or 'n' to stop.")

    # Printing the patient and procedure information.
    print("\nPatient and Procedure Information:")
    print(patient)
    for procedure in procedures:
        print()
        print(procedure)

if __name__ == "__main__":
    main()
