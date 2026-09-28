import turtle

''' This program uses the Turtle Graphics to generate two diamonds. '''

# Constant Values
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
TURTLE_SPEED = 2

# Turtle window size setup
turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT)

# Turtle setup
turtle.hideturtle()
turtle.fillcolor('blue')
turtle.speed(TURTLE_SPEED)

# Start with drawing the left-side diamond
turtle.begin_fill()
turtle.left(45)
turtle.backward(100)
turtle.right(90)
turtle.backward(100)
turtle.right(90)
turtle.backward(100)
turtle.right(90)
turtle.backward(100)

# Draw the right-side diamond after the left-side diamond is complete
turtle.backward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)

# Fill the shape color
turtle.end_fill()

# The turtle is finished.
print("Turtle complete.")
turtle.done()