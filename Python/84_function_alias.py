# function_alias_example.py
# This script demonstrates that in Python, functions are first-class objects.
# You can assign them to variables, pass them as arguments, and return them from other functions.
# This allows you to create aliases or alternative names for functions, making your code more flexible.

# In this example, we define a simple function to calculate the square of a number
# and then show how to use it in different ways.

def square(a):
    # This function returns the square of a number.
    return a ** 2

# Assign the function to a new variable
s = square  # Now, s points to the same function as square.

# You can call the function in two ways:
print(square(5))  # Calling square directly. This will print 25.

# Or, using the variable s that points to the same function:
print(s(5))  # This also calls the square function and prints 25.

# Checking the names of the functions:
print(s.__name__)  # This shows the name of the function s points to, which is 'square'.
print(square.__name__)  # This shows the name of the square function, which is also 'square'.

# Checking the memory addresses:
print(s)  # This shows the memory location of the function s.
print(square)  # This shows the same memory location as s, confirming they are the same function.
