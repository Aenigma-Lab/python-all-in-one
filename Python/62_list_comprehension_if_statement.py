# list comprehension with if statement
# just print even number with the help of list comph method.
# 


numbers = list(range(1,11))
# print(numbers)
even_num = [i for i in numbers if i%2==0]
print(even_num)


#list comprehension using odd number
odd_num = [i for i in list(range(1,21)) if i%2 != 0]
print(odd_num)
