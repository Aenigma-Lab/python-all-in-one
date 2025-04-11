# What is Decorators ?
# Decorators ----> enhace the functionality of other functions....
# decorators can take any function as argument.

# @ user for the decorators 



# suppose i have 2 funcions func_1() and func_2() and if i call one bye one it call that function 
# but without changing the function i want to add when func_1() call print extra line " i am awsome function."
# and when i call func_2() it also print extra line before "i am  awsome function." we can acheive this by generator without changing the func_1() and func_2()


# "i am awsome."

def func_1():
    print('this is function 1.')


def func_2():
    print('this is function 2.')

# here i want if i call any funcion " i am awsome" should print first without changing given function.

def decorator_func(any_function):
    def wrapper_function():
        print('i am awsome')
        any_function() # run any_function which is passed in decorator_func.
    return wrapper_function


var  = decorator_func(func_1)
var()

var = decorator_func(func_2)
var()
# we can call like this also
func_1 = decorator_func(func_1)
func_1()
# so here we have not changed the func_1() and func_2() code but enhance the functionality of both function wthout changing using decorators.

#############################################################################################################################
# Short cut to use decorators 
#
print("------------------------------------------------------------------")

# here i want if i call any funcion " i am awsome" should print first without changing given function.

def decorator_func_2(any_function):
    def wrapper_function():
        print('you are awsome')
        any_function() # run any_function which is passed in decorator_func.
    return wrapper_function



# "you are awsome."
@decorator_func_2
def func_3():
    print('this is function 1.')

#use @decorator_func4  to call func_4()
def func_4():
    print('this is function 2.')

func_3() # this is short cut 

# if we want to run fun_4 then we have to write @decorator_func_2  then func_4() wil also run