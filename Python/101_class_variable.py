#class variable
#circle
#are

class Circle:
    def __init__(self, radius ,pi):
        self.radius = radius
        self.pi = pi

    def area_of_circle(self):
        circle_area = 2*self.pi*self.radius*self.radius
        return circle_area

area = Circle(2,3.14)
print(f"Area of the circle {area.area_of_circle()}")


# So in above example we are not using the class variable so every time we have to pass 3.14 in every object and 
# if we have multiple object then it will every time crate memory of pi variable in every object.

 

class Another_Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        

    def circumfrence_of_circle(self):
        circle_area = 2*Another_Circle.pi*self.radius
        return circle_area

area_1 = Another_Circle(5)
print(f"circumferece of circle {area_1.circumfrence_of_circle()}")