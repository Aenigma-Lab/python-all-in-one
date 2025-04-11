# Importing wraps function from functools to preserve metadata of the original function
from functools import wraps

# This function is a decorator factory. It takes an argument `data_type` to specify 
# the allowed data type for the arguments passed to the decorated function.
def allowed_datatypes(data_type):
    
    # This is the actual decorator that will be applied to a function.
    def decorator(function):
        
        # This wrapper function is responsible for checking the types of the arguments
        # before calling the original function.
        @wraps(function)
        def wrapper(*args, **kwargs):
            
            # Check if all arguments passed to the function are of the allowed data_type
            if all([type(arg) == data_type for arg in args]):
                
                # If all arguments are of the correct type, call the function
                return function(*args, **kwargs)
            
            # If any argument is of an invalid type, print an error message
            print("Invalid Arguments: All arguments must be of type", data_type)
            return None
        
        # Return the decorated wrapper function
        return wrapper
    
    return decorator


# Define a function string_join that concatenates all the arguments into a single string
# In this case, no argument type checking is done in the function itself, it's just
# a simple string concatenation function.
@allowed_datatypes(str)  # Apply the decorator to check if all arguments are strings
def string_join(*args):
    string = ''
    for i in args:
        string += i  # Concatenate each argument to the string
    return string

# Example of calling the function with valid arguments
# All arguments passed are strings, so the function should work fine.
print(string_join('shubham', 'mishra', 'is', 'here'))  # Expected output: 'shubhammishraishere'

# Example of calling the function with an invalid argument
# The third argument is an integer, which should trigger the validation failure.
print(string_join('shubham', 'mishra', 1))  # Expected output: Invalid Arguments

# Example of calling the function with another invalid argument
# The second argument is a float, which should also trigger the validation failure.
print(string_join('Hello', 3.14, 'World'))  # Expected output: Invalid Arguments
