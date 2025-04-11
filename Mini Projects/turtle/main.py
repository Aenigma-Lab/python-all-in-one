# challenge
# draw a square line using turtle library.
# draw a dash line . - - - - - - - - - like this 
# draw a pentagon

from turtle import Turtle, Screen
# we can import this way also 
import turtle # if we want to write single time we can write this way
tom = turtle.Turtle()
# drawing a dash line 
# for _ in range(15):
#     tom.forward(10)
#     tom.pendown()
#     tom.forward(12)
#     tom.penup()
    

# drawing a square
from turtle import Turtle as T # Alias module
timmy = T()
# timmy.shape("turtle")
# timmy.color("red")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)



# timmy.right(100)

# draw triangle to deccan 

# for _ in range(3):
#     tom.color("blue")
#     tom.forward(100)
#     tom.left(120)
# for _ in range(4):
#     tom.color("red")
#     tom.forward(100)
#     tom.left(90)
# for _ in range(5):
#     tom.color("green")
#     tom.forward(100)
#     tom.left(72)
# for _ in range(6):
#     tom.color("black")
#     tom.forward(100)
#     tom.left(60)
# for _ in range(7):
#     tom.color("green")
#     tom.forward(100)
#     tom.left(52)
# for _ in range(8):
#     tom.color("orange")
#     tom.forward(100)
#     tom.left(45)
# for _ in range(9):
#     tom.color("green")
#     tom.forward(100)
#     tom.left(40)
# for _ in range(10):
#     tom.color("pink")
#     tom.forward(100)
#     tom.left(36)

#short code 
shapes = [
    (3, "blue"),
    (4, "red"),
    (5, "green"),
    (6, "black"),
    (7, "green"),
    (8, "orange"),
    (9, "green"),
    (10, "pink")
]

for sides, color in shapes:
    tom.color(color)
    angle = 360 / sides
    for _ in range(sides):
        tom.forward(100)
        tom.right(angle)

screen = Screen()
screen.exitonclick()