import turtle
import random

# Create turtle object
turt = turtle.Turtle()
turtle.colormode(255)  # Set color mode globally (for RGB colors)
turt.speed(50)
turt.pensize(15)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)  # Return RGB tuple

# Move the turtle randomly with different colors
for _ in range(300):
    turt.color(random_color())  # Set random color
    turt.forward(30)
    turt.setheading(random.choice(directions))

# Exit on click
screen = turtle.Screen()
screen.exitonclick()
