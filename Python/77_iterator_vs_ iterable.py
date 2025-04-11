#iterator vs iterables

# tuple, string, list --- are iterables.


numbers = [1,2,3,2,5] #iterables
squares = map(lambda a:a*2, numbers) #iterator

print(f" this will only print the map obj {squares}")#it will only print map object.

#how this loop work in object 
# 1. when loop run it call iter funciton
# 2. it call like this iter(numbers)-----> iterator
# 3. Then it will run  next(iter(number))----> here next funciton take 1 item at a time.

# example (it will print one by one)
number_iter = iter(numbers)
print(f"this is example of number_iter {next(number_iter)}")
print(f"this is example of number_iter {next(number_iter)}")
print(f"this is example of number_iter {next(number_iter)}")
print(f"this is example of number_iter {next(number_iter)}")
print(f"this is example of number_iter {next(number_iter)}")

# so we can call like this 
print(f"this is iterabor obj{next(squares)}")
print(f"this is iterabor obj{next(squares)}")
print(f"this is iterabor obj{next(squares)}")
# here directly list is not iterator object
print(next(number_iter))


#then it print like this in loop
for i in squares:
    print(i)


