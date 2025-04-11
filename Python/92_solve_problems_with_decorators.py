# from functools import wraps
# def allow_int(function):
#     @wraps(function)
#     def wrapper(*args,**kwargs):
#         data_types = []
#         for arg in args:
#             data_types.append(type(arg)==int)
#         if all(data_types):
#             return function(*args, **kwargs)
#         else:
#             print("Invalid Argument.")
#     return wrapper


# @allow_int       
# def add_all(*args):
#     total = 0
#     for i in  args:
#         total += i
#     return total

# print(add_all(1,2,3,4,5,[1,2,3]))


        
# Another method to run this function in short mode 

from functools import wraps
def allow_int(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        # data_types = []
        # for arg in args:
        #     data_types.append(type(arg)==int)
        # if all(data_types):
        #     return function(*args, **kwargs)
        # else:
        #     print("Invalid Argument.")
        if all([type(arg)== int for arg in args]):
            return function(*args, **kwargs)
        print("invalid input")

    return wrapper


@allow_int       
def add_all(*args):
    total = 0
    for i in  args:
        total += i
    return total

print(add_all(1,2,3,4,5))

