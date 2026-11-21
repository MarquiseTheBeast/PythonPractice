from pet import Pet

# Dog class
class Dog(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, 'Dog', 'Woof!')