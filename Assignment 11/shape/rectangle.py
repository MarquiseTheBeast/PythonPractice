from shape import Shape

# Rectangle class
class Rectangle(Shape):
    def __init__(self, shape, length, width):
        Shape.__init__(self, shape)
        self.__length = length
        self.__width = width
    
    # Return the area of rectangle.
    def get_area(self):
        area = self.__length * self.__width
        return area