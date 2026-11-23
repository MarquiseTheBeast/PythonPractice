from square import Square
from triangle import Triangle
from circle import Circle
from rectangle import Rectangle

def main():
    # List of shapes.
    shapes = [
        Rectangle("rect1", 4, 5),
        Circle("Circle", 3),
        Rectangle("rect1", 4, 4),
        Circle("Circle", 1.5),
        Square("Square", 4),
        Triangle("Triangle", 3, 4)
    ]

    # Return the shape name and its area value.
    print("Areas of various shapes:")
    for shape in shapes:  # polymorphism: each shape computes its own area
        print(f"{shape.__class__.__name__} area: {shape.get_area():.2f}")


if __name__ == "__main__":
    main()
