#lambda exression (anonymous function)

# normal function declearion 
def add(a,b):
    return a+b
print(add(3,4))


# Lambda function declearion.......
add2 = lambda a,b : a+b
print(add2(2,3))


# generally we use lambda expression with build in function.
#  like map, reduce, filter functions.

multiply  = lambda a,b : a*b
print(multiply(2,6))

print(add)
print(add2)
print(multiply)