#map function

# Explanation of the map function

# The map() function applies a specified function to each item of an iterable (like a list) 
# and returns a map object (which can be converted into a list, tuple, etc.).
# The syntax is:
# map(function, iterable)

# The function passed to map() can be a normal function, a lambda function, or any callable.

# Example 1: Finding the square of given numbers using a normal method
number = [1, 2, 3, 4]

def square(a):
    return a ** 2

# Manually applying the square function to each element
print(square(1), square(2), square(3), square(4))  # Output: 1 4 9 16

###or###################
final_square = []
for i in number:
    final_square.append(i**2)
print(f"find square of number using {final_square} using for loop")


# Example 2: Using the map function to apply the square function to a list
number1 = [2, 3, 4, 5]

# Using the same square function defined earlier
final_square = list(map(square, number1))
print(final_square)  # Output: [4, 9, 16, 25]


# Example 3: Using list comprehension to achieve the same result
number_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
final_square_list = [i ** 2 for i in number_list]
print(final_square_list)  # Output: [1, 4, 9, 25, 36, 49, 64, 81, 100]


# Example 4: Using lambda function with map
number2 = [1, 3, 5, 7, 9, 11, 13]
# Here we define a lambda function that squares its input
square_of_number = tuple(map(lambda a: a ** 2, number2))
print(square_of_number)  # Output: (1, 9, 25, 49, 81, 121, 169)


# More Examples of Using map()

# Example 5: Convert a list of strings to uppercase
string_list = ['hello', 'world', 'python']
upper_case_list = list(map(str.upper, string_list))
print(upper_case_list)  # Output: ['HELLO', 'WORLD', 'PYTHON']


# Example 6: Calculate the length of each string in a list
lengths = list(map(len, string_list))
print(lengths)  # Output: [5, 5, 6]


# Example 7: Using map with multiple iterables
# Here we will add corresponding elements of two lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_lists = list(map(lambda x, y: x + y, list1, list2))
print(sum_lists)  # Output: [5, 7, 9]


# Example 8: Applying a function that converts temperatures from Celsius to Fahrenheit
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)  # Output: [32.0, 50.0, 68.0, 86.0]



# # Here we are finding the square of given list numbers......with normal method

# number = [1,2,3,4]
# def square(a):
#     return a**2
# print(square(1),square(2),square(3),square(4))



# # Here i am using the map function to solve above give 

# number1 = [2,3,4,5]

# def find_square(a):
#     return a**2

# final_square = list(map(square,number1))
# print(final_square)


# # we can also do with list comphrension 

# number_list = [1,2,3,5,6,7,8,9,10]
# final_square_list = [i**2 for i in number_list]
# print(final_square_list)

# # more proper this this we can use lambda function insted  of find_square() function
# # ex 
number2 = [1,3,5,7,9,11,13]
square_of_number = tuple(map(lambda a: a**2, number2))
print(square_of_number)



# Quesiton : Find the length of every string in given list
# map object is iterator .........
student_names = ['chandra','mohan','sohan','kausal','gubber']
lenght = map(len, student_names)
for i in lenght:
    print(i)

for j in lenght:
    print(j)
