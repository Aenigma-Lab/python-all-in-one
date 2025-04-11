# Step 1: Define the Person class
class Person:
    # Step 2: The __init__ method is called when we create an instance of the Person class
    # It initializes the object with the values passed as arguments.
    def __init__(self, first_name, last_name, age):
        # The self keyword refers to the current instance of the class
        # self.first_name, self.last_name, and self.age are instance variables
        # These variables store the values passed to the __init__ method.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    # Step 3: Define an instance method called full_name
    def full_name(self):
        # This method returns a string that combines the first and last names
        # self.first_name refers to the first_name attribute of the current object
        # self.last_name refers to the last_name attribute of the current object
        return f"{self.first_name} {self.last_name}"

# Step 4: Create two instances (objects) of the Person class
p1 = Person('Shubham', 'Mishra', 24)  # Creating an object 'p1' with specific data
p2 = Person('Raghav', 'Kumar', 27)    # Creating another object 'p2' with different data

# Step 5: Calling the full_name method using p1 object
# p1 is an instance of the Person class
# When we call p1.full_name(), Python will pass p1 as the 'self' argument inside the full_name method
print(p1.full_name())  # Expected output: "Shubham Mishra"
# Explanation: 
# - p1.first_name = "Shubham"
# - p1.last_name = "Mishra"
# The method returns "Shubham Mishra"

# Step 6: Calling the full_name method using the Person class and passing p2 as an argument
# You can call instance methods through the class itself by passing an object (p2) as the first argument
print(Person.full_name(p2))  # Expected output: "Raghav Kumar"
# Explanation:
# - Python automatically passes p2 as the 'self' argument to full_name
# - Inside full_name, self refers to p2
# - p2.first_name = "Raghav"
# - p2.last_name = "Kumar"
# The method returns "Raghav Kumar"

# Step 7: Calling the full_name method using the Person class and passing p1 as an argument
# Similarly, you can also call the full_name method through the class by passing p1 as the first argument
print(Person.full_name(p1))  # Expected output: "Shubham Mishra"
# Explanation:
# - Python automatically passes p1 as the 'self' argument to full_name
# - Inside full_name, self refers to p1
# - p1.first_name = "Shubham"
# - p1.last_name = "Mishra"
# The method returns "Shubham Mishra"

# Conclusion:
# - In this code, we created a class Person with an instance method 'full_name'.
# - The 'full_name' method is used to print a person's full name by combining their first and last name.
# - We demonstrated two ways to call this instance method:
#    1. Using the object directly (e.g., p1.full_name())
#    2. Using the class name and passing the object explicitly (e.g., Person.full_name(p1))



# lets check predefine class ------------how the passing object

# example :

my_list = [1,2,3,4,5]
# ex: we using clear and pop in out list 

my_list.clear() #-----this is one way that use use to clear the list 
print(my_list)
############################## another way to clear on root level  #####
list.clear(my_list) # we can write this way also 
print(my_list)

############################# append data in list##############3
my_list.append(6)
list.append(my_list,7) # we can write this way also !imp-----

print(my_list)