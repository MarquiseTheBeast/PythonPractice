from shape import Shape

# Triangle class
class Triangle(Shape):
    def __init__(self, shape, base, height):
        Shape.__init__(self, shape)
        self.__base = base
        self.__height = height

    # Return the area of triangle.
    def get_area(self):
        area = (self.__base * self.__height) / 2
        return area