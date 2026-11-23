from pet import Pet

# Dog class
class Dog(Pet):
    def __init__(self, name):
        Pet.__init__(self, name)

    def make_sound(self):
        print(f"{self.get_name()} the Dog says Woof!")