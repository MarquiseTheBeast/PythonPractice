# Patient class
class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact, emergency_phone_number):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact = emergency_contact
        self.__emergency_phone_number = emergency_phone_number

    # Return patient's first name.
    def get_first_name(self):
        return self.__first_name

    # Return patient's middle name.
    def get_middle_name(self):
        return self.__middle_name

    # Return patient's last name.
    def get_last_name(self):
        return self.__last_name

    # Return patient's address.
    def get_address(self):
        return self.__address

    # Return city.
    def get_city(self):
        return self.__city

    # Return state.
    def get_state(self):
        return self.__state

    # Return zip code.
    def get_zip_code(self):
        return self.__zip_code

    # Return patient's phone number.
    def get_phone_number(self):
        return self.__phone_number

    # Return patient's emergency contact.
    def get_emergency_contact(self):
        return self.__emergency_contact

    # Return patient's emergency phone number.
    def get_emergency_phone_number(self):
        return self.__emergency_phone_number
    
    # Set first name.
    def set_first_name(self, first_name):
        self.__first_name = first_name

    # Set middle name.
    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    # Set last name.
    def set_last_name(self, last_name):
        self.__last_name = last_name

    # Set address.
    def set_address(self, address):
        self.__address = address

    # Set city.
    def set_address(self, city):
        self.__city = city

    # Set zip code.
    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    # Set phone number.
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    # Set emergency contact.
    def set_emergency_contact(self, emergency_contact):
        self.__emergency_contact = emergency_contact

    # Set emergency phone number.
    def set_emergency_phone_number(self, emergency_phone_number):
        self.__emergency_phone_number = emergency_phone_number

    def __str__(self):
        # String for first name, middle name, and last name.
        str1 = (f"First Name: {self.__first_name}\nMiddle Name: {self.__middle_name}\nLast Name: {self.__last_name}")

        # String for address, city, state, zip code, and phone number.
        str2 = (f"Address: {self.__address}\nCity: {self.__city}\nState: {self.__state}\nZIP: {self.__zip_code}\nPhone: {self.__phone_number}")
        
        # String for emergency contact and emergency phone number.
        str3 = (f"Emergency Contact: {self.__emergency_contact}\nEmergency Phone: {self.__emergency_phone_number}")

        string = str1 + '\n' + str2 + '\n' + str3
        return string