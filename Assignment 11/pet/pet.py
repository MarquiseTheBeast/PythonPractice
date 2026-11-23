# Pet class
class Pet:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def make_sound(self):
        print(f"Regular animal says Grrrr!")