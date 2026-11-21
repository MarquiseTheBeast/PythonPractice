# Shape class
class Shape:
    def __init__(self, shape):
        self.__shape = shape

    # Set shape
    def set_shape(self, shape):
        self.__shape = shape

    # Return shape
    def get_shape(self):
        return self.__shape

    # Return area
    def get_area(self):
        return 1