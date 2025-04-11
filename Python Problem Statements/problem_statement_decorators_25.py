# calculate total time taken to execute a function using decorators
import time
from functools import wraps
def calculate_time(function):
    @wraps(function)
    def wrapper_function(*args, **kwargs):
       t1 = time.time()
       returned_function = function(*args, **kwargs)
       t2 = time.time()
       total_time  = t2-t1
       print(f'total time taken to execute the function {total_time}')
       return returned_function
    return wrapper_function
        
        

@calculate_time
def calculate_square(numbers):
  square  = [i**2 for i in range(1,numbers+1) ]
  print(square)

calculate_square(10)