# DOCSTRINGS 

# Docstrings are special notes that explain what a function does.
# They help people understand your code.

# To write a docstring, use triple quotes (""") right after the function name.
# Inside, you can describe what the function does.

def add(a, b):
    '''This function adds two numbers and gives you their sum.
    
    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    '''
    return a + b

# You can see the docstring by using __doc__ with the function.
print(add.__doc__)

# Some built-in functions in Python are:
# len(), sum(), max(), min(), sorted()

# You can check the docstring for these functions too.

print(len.__doc__)  # Shows what the len function does.
print(sum.__doc__)  # Shows what the sum function does.



# The help function shows you more details about the function.
help(sum)

# help(len)
