# In programming, a function is a reusable block of code that performs a specific task.
# Functions help organize code, make it more readable, and avoid repetition.
# They take inputs (often called parameters or arguments), process them, and can return an output.

# Basic Structure of a Function:
# 1. Function Definition: 
#    - The 'def' keyword is used to define a function, followed by the function name and parentheses.
#    - Inside the parentheses, you can define parameters.
# 2. Function Body:
#    - The block of code within the function that performs the task.
# 3. Return Statement:
#    - The 'return' keyword is used to send the result back from the function.


# Define a function named 'add_two_numbers'
# This function takes two parameters: 'a' and 'b'
def add_two_numbers(a, b):
    # Inside the function body, add 'a' and 'b' together
    result = a + b
    # Return the result of the addition
    return result

# Call the function 'add_two_numbers' with arguments 10 and 12
# The returned value is assigned to the variable 'total'
total = add_two_numbers(10, 12)

# Print the value of 'total' to see the result
print(total)


##############################################################
# take from user input

num1, num2 = map(int,input("Enter first & second number for addition.").split(" "))

def add(num1, num2):
    return num1+num2

print(add(num1, num2))