
from functools import wraps
def decorator_function(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        """this is wrapper function"""
        print(f'you are calling {function.__name__} function')
        print(f'{function.__doc__}')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def add(a,b):
    '''this is add function adding of two numbers.'''
    return a+b




print(add.__doc__)# this should print doc string inside the add function.
print(add.__name__)# this should print add function name

# print(decorator_function.__doc__)
print(decorator_function.__name__)# this should print decorator_function name.


# while I print doc of add function with decorator it printing the doc of decorator_function to fix this issue we use import. 
# -- if you can't understand this statement comment the import and also comment the @wrap(any_function).
