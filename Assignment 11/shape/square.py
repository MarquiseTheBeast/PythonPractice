from shape import Shape

# Square class
class Square(Shape):
    def __init__(self, shape, side):
        Shape.__init__(self, shape)
        self.__side = side
    
    # Return the area of square.
    def get_area(self):
        area = self.__side**2
        return area