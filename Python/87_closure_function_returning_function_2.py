# Function returning function (closure) practice

# suppose we want to make function that return square  , and another funciton that return cube and another that adding some values
# so insted of makeing multiple function we can make one function only.
# to perform eg: square, cube , addition , raisetopower4------>  will make only one funcion 

# we will use funciton returning function 

def to_power(x):  # x= 3
    def cal_power(n): # n = 2
        return n**x
    return cal_power

cube = to_power(3)
print(cube(2))

square = to_power(2)
print(4)