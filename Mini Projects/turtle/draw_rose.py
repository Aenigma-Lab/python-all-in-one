import turtle as t


def draw_petal():
    t.begin_fill()
    for _ in range(2):
        t.circle(50, 60)
        t.left(120)
    t.end_fill()

def draw_rose():
    t.speed(0)
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("red")
    t.fillcolor("red")
    for _ in range(8):
        draw_petal()
        t.right(45)

def draw_stem():
    t.color("green")
    t.pensize(5)
    t.right(90)
    t.forward(150)
    t.right(20)
    t.forward(50)

def draw_leaf(x, y, angle):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("green")
    t.fillcolor("green")
    t.begin_fill()
    t.right(angle)
    t.circle(30, 90)
    t.left(90)
    t.circle(30, 90)
    t.left(90)
    t.end_fill()

def draw_flower():
    draw_rose()
    draw_stem()
    draw_leaf(-20, -100, 45)
    draw_leaf(20, -120, -45)

t.bgcolor("white")

t.pensize(2)
t.speed(3)
draw_flower()
t.done()










