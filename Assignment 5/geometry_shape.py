import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"

def main():
    #TODO: reference lecture5 slide#65 to call the function to draw the requested shape until user chooses to quit

    # Displays the shape menu
    display_menu()

    # loop until input selection is QUIT
    while (choice_input := input("Enter your choice: ")) != QUIT:
        if choice_input == SQUARE:
            # User will input the starting X coordinate, starting Y coordinate, length of side, and fill color of the square.
            starting_x_coordinate = float(input("Enter the starting X coordinate: "))
            starting_y_coordinate = float(input("Enter the starting Y coordinate: "))
            side_length = float(input("Enter the length of a side: "))
            fill_color_selection = input("Enter fill color: ")

            # Clear everything on the turtle window before drawing the shape
            turtle.reset()

            # Pass variables in function before starting to draw the shape.
            square(starting_x_coordinate, starting_y_coordinate, side_length, fill_color_selection)
            print("Square drawing complete!")
            display_menu()
        elif choice_input == CIRCLE:
            # User will input the starting X coordinate, starting Y coordinate, radius value, and fill color of the circle.
            starting_x_coordinate = float(input("Enter the starting X coordinate: "))
            starting_y_coordinate = float(input("Enter the starting Y coordinate: "))
            radius_value = float(input("Enter the radius: "))
            fill_color_selection = input("Enter fill color: ")

            # Clear everything on the turtle window before drawing the shape
            turtle.reset()

            # Pass variables in function before starting to draw the shape.
            circle(starting_x_coordinate, starting_y_coordinate, radius_value, fill_color_selection)
            print("Circle drawing complete!")
            display_menu()
        elif choice_input == TRIANGLE:
            # # User will input the starting X coordinate, starting Y coordinate, length of side, and fill color of the equilaterial triangle.
            starting_x_coordinate = float(input("Enter the starting X coordinate: "))
            starting_y_coordinate = float(input("Enter the starting Y coordinate: "))
            side_length = float(input("Enter the length of a side: "))
            fill_color_selection = input("Enter fill color: ")

            # Clear everything on the turtle window before drawing the shape
            turtle.reset()

            # Pass variables in function before starting to draw the shape.
            equilateral_triangle(starting_x_coordinate, starting_y_coordinate, side_length, fill_color_selection)
            print("Equilaterial drawing complete!")
            display_menu()
        else:
            # Display menu will show again as the user will input choice selection again until the input selection is valid
            print("Invalid input: Please enter 1, 2, 3, or 4.")
            display_menu()

    print("Exiting the program.")

def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")

#TODO: copy the code from lecture5 slide# 69
def square(x, y, side, color):
    turtle.penup() # Raise the pen
    turtle.goto(x, y) # Move to (X,Y)
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown() # Lower the pen
    turtle.begin_fill() # Start filling

    for count in range(4): # Draw a square
        turtle.forward(side)
        turtle.left(90)

    turtle.end_fill() 
    pass
   
def equilateral_triangle(x, y, side, color):
    # draw a triangle starting coordinate at x,y
    turtle.penup()              
    turtle.goto(x, y)           
    turtle.fillcolor(color)     
    turtle.pendown()            
    turtle.begin_fill()         
    for count in range(3):      
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

#TODO: copy lecture slide 71 code
def circle(x, y, radius, color):
    turtle.penup() # Raise the pen
    turtle.goto(x, y - radius) # Position the turtle
    turtle.fillcolor(color) # Set the fill color
    turtle.pendown() # Lower the pen
    turtle.begin_fill() # Start filling
    turtle.circle(radius) # Draw a circle
    turtle.end_fill() # End filling
    pass

if __name__ == "__main__":
    main()
