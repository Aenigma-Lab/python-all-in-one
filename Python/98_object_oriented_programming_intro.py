# Object-Oriented Programming (OOP) - Comprehensive Explanation

# OOP is a programming paradigm based on the concept of objects, which have data (attributes) and behavior (methods).
# It is used in many popular programming languages, such as Python, C++, Java, etc. 
# The basic idea of OOP is to model real-world entities using objects and classes.

# Key Concepts of OOP:
# 1. Class
# 2. Object (Instance)
# 3. Method
# 4. Encapsulation
# 5. Inheritance
# 6. Polymorphism
# 7. Abstraction

# Let's define a simple example to explain all of these concepts.


# 1. CLASS: A blueprint for creating objects (instances).
class Car:
    # Constructor (__init__) method initializes the attributes of the object.
    def __init__(self, brand, model, year):
        self.brand = brand  # Instance attribute: brand of the car
        self.model = model  # Instance attribute: model of the car
        self.year = year    # Instance attribute: manufacturing year of the car

    # Method to display the car information
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")

    # Method to start the car engine
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now running.")

    # Method to stop the car engine
    def stop_engine(self):
        print(f"The {self.brand} {self.model}'s engine is now off.")


# 2. OBJECT (INSTANCE): Objects are instances of a class. They are created from the class blueprint.
car1 = Car("Toyota", "Corolla", 2022)  # Creating an object of the Car class
car2 = Car("Honda", "Civic", 2023)    # Creating another object of the Car class

# 3. METHOD: Methods are functions defined within a class that describe the behaviors of the object.
car1.display_info()  # Output: 2022 Toyota Corolla
car1.start_engine()  # Output: The Toyota Corolla's engine is now running.
car1.stop_engine()   # Output: The Toyota Corolla's engine is now off.

car2.display_info()  # Output: 2023 Honda Civic
car2.start_engine()  # Output: The Honda Civic's engine is now running.


# 4. ENCAPSULATION: Restricting access to some components and only exposing necessary parts.
# This can be done by using private attributes and getter/setter methods.
class CarWithEncapsulation:
    def __init__(self, brand, model, year):
        self.__brand = brand  # Private attribute (cannot be accessed directly)
        self.model = model
        self.year = year

    # Getter method to access the private attribute __brand
    def get_brand(self):
        return self.__brand

    # Setter method to modify the private attribute __brand
    def set_brand(self, brand):
        self.__brand = brand

    def display_info(self):
        print(f"{self.year} {self.__brand} {self.model}")


car3 = CarWithEncapsulation("BMW", "X5", 2022)
car3.display_info()  # Output: 2022 BMW X5

# Trying to access the private attribute __brand directly will result in an error
# print(car3.__brand)  # This will raise an AttributeError

# Using getter and setter methods
print(car3.get_brand())  # Output: BMW
car3.set_brand("Audi")
print(car3.get_brand())  # Output: Audi


# 5. INHERITANCE: Inheritance allows a class to inherit attributes and methods from another class.
# The new class (child class) can reuse the code of the parent class and add or modify its own behavior.

# Base class
class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand}")

# Derived class that inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)  # Calling the constructor of the parent class
        self.model = model

    # Overriding the display_info method from the parent class
    def display_info(self):
        super().display_info()  # Calling the parent class's method
        print(f"Model: {self.model}")

# Creating objects of the derived class
vehicle1 = Vehicle("Toyota", 2022)
vehicle1.display_info()  # Output: 2022 Toyota

car4 = Car("Honda", 2023, "Civic")
car4.display_info()  # Output: 2023 Honda
                     #         Model: Civic


# 6. POLYMORPHISM: The ability of different classes to respond to the same method in different ways.
# This can be achieved through method overriding (changing behavior of a method in the child class).
# Another example is method overloading, but Python does not support method overloading by default.

# Example of method overriding (already demonstrated in the Car class above)

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

# Polymorphism in action: Same method name, different behavior
animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()  # Output: Animal makes a sound
dog.speak()     # Output: Dog barks
cat.speak()     # Output: Cat meows


# 7. ABSTRACTION: Abstraction is the concept of hiding the complex implementation details and showing only the necessary features.
# In Python, we can achieve abstraction using abstract classes and methods from the abc (Abstract Base Class) module.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating objects of the subclasses
circle = Circle(5)
rectangle = Rectangle(4, 6)

print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 78.5
print(f"Rectangle Area: {rectangle.area()}")  # Output: Rectangle Area: 24


# Summary of OOP concepts demonstrated:
# - Class: A blueprint for creating objects.
# - Object: An instance of a class.
# - Method: A function inside a class that describes the behaviors of the object.
# - Encapsulation: Hiding details using private attributes and getter/setter methods.
# - Inheritance: Reusing code from another class.
# - Polymorphism: Same method name, but different behaviors in different classes.
# - Abstraction: Hiding complex details and exposing only necessary features.
