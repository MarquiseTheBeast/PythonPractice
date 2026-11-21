from pet import Pet

# Cat class
class Bird(Pet):
    def __init__(self, name):
        Pet.__init__(self, name, 'Bird', 'Tweet!')