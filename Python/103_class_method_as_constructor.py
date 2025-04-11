# Define the 'Person' class
class Person:
    
    # Class attribute to count the number of instances created
    count_instance = 0  # This is a class variable, shared across all instances of the class

    # The __init__ method is the constructor that gets called when an instance is created
    def __init__(self, first_name, last_name, age):
        # Each time a new instance is created, increment the count_instance
        Person.count_instance += 1  # Access the class variable to keep track of how many instances are created
        
        # Assign instance variables to store the attributes for the instance
        self.first_name = first_name  # Instance variable for the first name
        self.last_name = last_name    # Instance variable for the last name
        self.age = age                # Instance variable for age
    
    # A class method to create an instance from a comma-separated string
    @classmethod
    def from_string(cls, string):
        # Split the string by commas, and assign the values to first, last, and age
        first, last, age = string.split(',')
        
        # Return a new instance of the class using the class method, passing the extracted data
        return cls(first, last, int(age))  # Convert the 'age' to an integer and pass it to the constructor
    
    # An instance method to return the full name of the person
    def full_name(self):
        # Access the instance variables to return a string combining the first and last name
        return f"{self.first_name} {self.last_name}"
    
    # Another instance method to check if the person is above 18 years of age
    def is_above_18(self):
        # Compare the 'age' instance variable with 18 and return True or False
        return self.age > 18
    
    # A class method to return the number of instances of the Person class created
    @classmethod
    def count_instances(cls):
        # Access the class variable 'count_instance' to get the number of instances
        return f"You have created {cls.count_instance} instance(s) of {cls.__name__}."  # Use __name__ to get the class name ('Person')

# Create an instance of the Person class using the constructor (__init__ method)
p1 = Person('Shubham', 'Mishra', 25)  # First name is 'Shubham', last name is 'Mishra', and age is 25
p2 = Person('Ashish', 'Kumar', 55)    # Another instance with first name 'Ashish', last name 'Kumar', and age 55

# Create an instance using the 'from_string' class method
p3 = Person.from_string('Amrendra,Bahubali,28')  # The string 'Amrendra,Bahubali,28' is split into first name, last name, and age

# Print the full name of the third instance using an instance method
print(p3.full_name())  # This will call p3.full_name(), which returns 'Amrendra Bahubali'

# Print the count of instances created using the class method
print(Person.count_instances())  # This will call the class method count_instances() to display the number of instances created


########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################

# Class Method Examples in Python

class Person:
    count = 0  # A class variable to count the number of Person instances

    def __init__(self, name):
        self.name = name
        Person.increment_count()

    @classmethod
    def increment_count(cls):
        # Class method to increment the count of instances
        cls.count += 1

    @classmethod
    def get_count(cls):
        # Class method to return the current count of instances created
        return cls.count


# Example 1: Basic Class Method (increment and get count of instances)
p1 = Person("Alice")
p2 = Person("Bob")

# Access class method using class name
print("Total Person Instances:", Person.get_count())  # Output: 2

# Access class method using an instance (though it's better to call it on the class)
print("Total Person Instances via instance:", p1.get_count())  # Output: 2



class Car:
    total_cars = 0  # Class variable to track total number of cars

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.add_car()

    @classmethod
    def add_car(cls):
        # Class method to add one to the total_cars class variable
        cls.total_cars += 1

    @classmethod
    def get_total_cars(cls):
        # Class method to return the total number of cars created
        return cls.total_cars


# Example 2: Class Method to Modify Class State (track total cars)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Focus")

# Access class method to get the total number of cars
print("Total Cars Created:", Car.get_total_cars())  # Output: 3



class PersonFactory:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_string):
        # Factory method to create an instance of Person from a string
        name, age = data_string.split(", ")
        return cls(name, int(age))


# Example 3: Class Method as a Factory Method (creating an instance from a string)
person_str = "Alice, 30"
person1 = PersonFactory.from_string(person_str)
print(f"Name: {person1.name}, Age: {person1.age}")  # Output: Name: Alice, Age: 30



class Animal:
    species = "Unknown"  # Class variable

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_species(cls):
        # Class method to get the species of the animal (from the class)
        return cls.species

class Dog(Animal):
    species = "Canine"  # Overriding the species for Dog

class Cat(Animal):
    species = "Feline"  # Overriding the species for Cat


# Example 4: Class Method with Inheritance (modifying class state in subclass)
print("Animal species:", Animal.get_species())  # Output: Unknown
print("Dog species:", Dog.get_species())  # Output: Canine
print("Cat species:", Cat.get_species())  # Output: Feline



class Library:
    books = []  # Class variable to hold a list of books

    @classmethod
    def add_book(cls, book_name):
        # Class method to add a book to the library
        cls.books.append(book_name)

    @classmethod
    def display_books(cls):
        # Class method to return the list of books
        return cls.books


# Example 5: Class Method to Modify Class State (manage a library)
Library.add_book("The Great Gatsby")
Library.add_book("1984")
Library.add_book("Moby Dick")

# Display the books in the library
print("Books in Library:", Library.display_books())  # Output: ['The Great Gatsby', '1984', 'Moby Dick']



# Explanation of Key Points:

# 1. **Access to Class State**:
#    - The class method uses `cls` to refer to the class and can modify class-level attributes.
#    - For example, `get_total_cars` in the `Car` class accesses the class variable `total_cars` to return the number of cars created.

# 2. **Called on Class or Instance**:
#    - Class methods can be called either using the class name (e.g., `Person.get_count()`) or an instance (e.g., `p1.get_count()`).
#    - It is typically more meaningful to call class methods on the class itself, especially if they modify or access class-level state, as in `Car.get_total_cars()`.

# 3. **Factory Method**:
#    - Class methods can be used as factory methods to provide different ways of creating instances of the class.
#    - For instance, in the `PersonFactory` class, the `from_string` method parses a string and creates a `PersonFactory` object from it, providing an alternative way of instantiating the class.

# 4. **Inheritance**:
#    - Class methods are inherited by subclasses, and they can be overridden to modify the behavior in the subclass context.
#    - In the example with `Animal`, the `get_species` method is inherited by both `Dog` and `Cat` subclasses, but the `species` variable is overridden to reflect the correct species for each subclass.

# 5. **Modify Class State**:
#    - Class methods can modify or access shared data across all instances of the class, like the `total_cars` in the `Car` class or the `books` in the `Library` class.
#    - These modifications affect all instances of the class, and can be used for managing data that is not specific to a particular instance, but rather to the class as a whole.
