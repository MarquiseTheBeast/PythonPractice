from pet import Pet

# Cat class
class Cat(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, 'Cat', 'Meow!')