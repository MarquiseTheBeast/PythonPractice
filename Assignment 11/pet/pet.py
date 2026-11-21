# Pet class
class Pet:
    def __init__(self, name, species, sound):
        self.__name = name
        self.__species = species
        self.__sound = sound

    def make_sound(self):
        return f"{self.__name} the {self.__species} says {self.__sound}"