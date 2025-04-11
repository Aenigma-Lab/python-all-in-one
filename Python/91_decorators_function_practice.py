from functools import wraps
def print_function_data(any_type_function):
    '''this is decorator of print function data.'''
    @wraps(any_type_function)
    def wrap_function(*args, **kwargs):
        print('this is wrap function inside the decorator function')
        print(f'you are calling {any_type_function.__name__} function')
        print(f'{any_type_function.__doc__}')
        return any_type_function(*args, **kwargs)
    return wrap_function





@print_function_data
def add(a,b):
    '''this function take two number as argument and return their sum'''
    return a+b

add = print_function_data(add)
print(add(2,4))