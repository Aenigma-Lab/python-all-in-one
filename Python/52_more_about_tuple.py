# something more about tuple like list, string.


num = tuple(range(1,11)) # it will give output in tuple
print(f" this is 'tuple' {num} and its type is {type(num)}")


num2 = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) #convert tuple to list. Here we will give 2 bracket otherwise it will give error
print(f" this is 'list' {num2} and its type is {type(num2)}")


num3 = str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# "((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))" # it is written like this.
print(f" this is not tuple it is 'string' {num3} and its type is {type(num3)}")


num4 = tuple([1,2,3,4,6,7,8])
print(f" converting list to 'tuple'{num4} and its type is {type(num4)}")