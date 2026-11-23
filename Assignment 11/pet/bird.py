from pet import Pet

# Cat class
class Bird(Pet):
    def __init__(self, name):
        Pet.__init__(self, name)

    def make_sound(self):
        print(f"{self.get_name()} the Bird says Tweet!")