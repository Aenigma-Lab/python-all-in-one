def decorator_function(any_function):
    def wrapper_function(*args, **kwargs):
        print('this is awesome function')
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def func(a):
    print(f'this is function with argument {a}.')


@decorator_function
def addition(a,b):
    return a+b

print(addition(7,9))


# func = decorator_function(func)
func(8)