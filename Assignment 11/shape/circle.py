from shape import Shape
import math

# Circle class
class Circle(Shape):
    def __init__(self, shape, radius):
        Shape.__init__(self, shape)
        self.__radius = radius
    
    # Return the area of circle.
    def get_area(self):
        area = math.pi * self.__radius**2
        return area