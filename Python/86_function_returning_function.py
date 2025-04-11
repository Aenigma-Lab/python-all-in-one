# This function demonstrates how to return a nested function from an outer function.
def outer_function():
    # Inner function that prints a message
    def inner_function():
        print('inside inner function')
    # Return the inner function without calling it
    return inner_function

# Store the returned inner function in the variable `var`
var = outer_function()  # Here, `var` stores the inner function but does not execute it.
var()  # This will execute `inner_function()` and print the message.

#######################################################
# If we return the inner function with parentheses,
# it will be executed immediately, and we won't store the function itself.
def outer_function_immediate():
    def inner_function():
        print('inside inner function')
    # Call the inner function immediately and return its result
    return inner_function()  # This will execute the function and return None

var_immediate = outer_function_immediate()  # Here, `var_immediate` will store the result of the print statement, which is None.

#############################################################
# Another Example: This time the outer function takes an argument.
def outer_function_2(msg):
    # Inner function that prints a message using the argument from the outer function
    def inner_function_2():
        print(f"message is {msg}")
    # Return the inner function without calling it
    return inner_function_2

# Store the returned inner function in the variable `var_2` with a specific message
var_2 = outer_function_2("hi there, how are you!")  # This stores the inner function.
var_2()  # This will execute `inner_function_2()` and print the message.
