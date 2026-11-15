# Pet class
class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__type = animal_type
        self.__age = age

    # Return name.
    def get_name(self):
        return self.__name

    # Return the type of animal.
    def get_animal_type(self):
        return self.__type

    # Return age.
    def get_age(self):
        return self.__age

    # Set name.
    def set_name(self, name):
        self.__name = name

    # Set the type of animal.
    def set_animal_type(self, animal_type):
        self.__type = animal_type

    # Set age.
    def set_age(self, name):
        self.__age = name

    # Return string of pet's name, animal type, and age. 
    def __str__(self):
        return (f"Pet Name: {self.__name}\nAnimal Type: {self.__type}\nAge of Pet: {self.__age}")

    