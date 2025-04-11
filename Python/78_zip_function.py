# Zip Function in Python

"""
Definition of zip in Python:

The zip() function is a built-in utility that takes multiple iterables (like lists, tuples, or strings)
and returns an iterator of tuples. Each tuple contains elements from the input iterables that share
the same index, allowing for convenient grouping of elements based on their position.

Syntax:
    zip(*iterables)

Parameters:
    - iterables: One or more iterable objects (like lists, tuples, or strings). They can be of different lengths.

Returns:
    An iterator of tuples, where the i-th tuple contains the i-th elements from each of the input iterables.
    If the input iterables are of unequal length, zip stops creating tuples when the shortest input iterable is exhausted.
"""

# Example 1: Basic Usage of zip with Two Lists
user_id = ['user1', 'user2', 'user3', 'user4']
name = ['shubham', 'mohit', 'aman', 'raman']

# Displaying the zip object (it won't show the actual zipped content)
print("Example 1: Basic Usage of zip")
print(zip(user_id, name))  # Output: <zip object at 0x...>

# To get the values from the zip object, convert it to a list
zipped_list = list(zip(user_id, name))
print(zipped_list)  
# Output: [('user1', 'shubham'), ('user2', 'mohit'), ('user3', 'aman'), ('user4', 'raman')]

# Example 2: Handling Different Lengths of Lists
print("\nExample 2: Handling Different Lengths of Lists")
userid = ['usr1', 'usr2', 'usr3']
names = ['alfa', 'beta']
# It will not zip 'usr3' because there's no corresponding name
zipped_tuple = tuple(zip(userid, names))
print(zipped_tuple)  
# Output: (('usr1', 'alfa'), ('usr2', 'beta'))

# Example 3: Converting a List of Tuples into a Dictionary
print("\nExample 3: Converting a List of Tuples into a Dictionary")
example = [('a', 1), ('b', 2), ('c', 3)]
converted_dict = dict(example)
print(converted_dict)  
# Output: {'a': 1, 'b': 2, 'c': 3}

# Example 4: Zipping Multiple Lists
print("\nExample 4: Zipping Multiple Lists")
id = [1, 2, 3, 4]
first_name = ['shubham', 'alfa', 'beta', 'gamma']
last_name = ['mishra', 'singh', 'kumar', 'more']

# Zipping more than two lists
zipped_multiple = list(zip(id, first_name, last_name))
print(zipped_multiple)  
# Output: [(1, 'shubham', 'mishra'), (2, 'alfa', 'singh'), (3, 'beta', 'kumar'), (4, 'gamma', 'more')]

# Converting the first two zipped lists into a dictionary
dict_from_zip = dict(zip(id, first_name))
print(dict_from_zip)  
# Output: {1: 'shubham', 2: 'alfa', 3: 'beta', 4: 'gamma'}

# Example 5: Attempting to Convert Zipped Tuples of Length Greater than 2 to a Dictionary
print("\nExample 5: Attempting to Convert Zipped Tuples of Length Greater than 2 to a Dictionary")
# This will raise a TypeError as dict() expects pairs
# Uncommenting the next line will raise TypeError
# print(dict(zip(id, first_name, last_name)))  # Uncommenting this line will raise TypeError

# Example 6: Unzipping a List of Tuples
print("\nExample 6: Unzipping a List of Tuples")
unzipped = list(zip(*zipped_multiple))
print(unzipped)  
# Output: [(1, 2, 3, 4), ('shubham', 'alfa', 'beta', 'gamma'), ('mishra', 'singh', 'kumar', 'more')]

# Summary
"""
- zip() combines multiple iterables into tuples based on their index.
- If the iterables are of different lengths, zip() stops at the shortest one.
- Use dict() to convert tuples of length 2 into a dictionary.
- Multiple lists can be zipped together, but you can only convert pairs to a dictionary.
- You can also unzip tuples back into separate lists using the unpacking operator (*).
"""








user_id = ['user1','user2','user3','user4']
name = ['shubham','mohit','aman','raman']

#('user1','shubham'),('user2','mohit')#zip object give this type of output

print(zip(user_id,name)) # this will print zip object "<zip object at 0x7bf6c94adf80>"

# to get value from zip object
print(list(zip(user_id,name))) 

# take anothe example if user id is less then user name

userid = ['usr1','usr2','usr3']
names = ['alfa','beta']
#it will not zip usr3 because user3 combination is not present in name
# here only 2 names is preset so it will zip only 2

print(tuple(zip(userid,names)))


# another example 

# if we have  [()] tuple in insdie the list we can convert in dict.

example = [('a',1),('b',2),('c',3)]
print(dict(example)) #output {'a': 1, 'b': 2, 'c': 3}


#another example if we have multiple lists

id = [1,2,3,4]
first_name = ['shubham','alfa','beta','gamma']
last_name = ['mishra','singh','kumar','more']
# we can zip more then 2 list 
print(list(zip(id,first_name,last_name)))

print(dict(zip(id,first_name)))


# we can not convert this to dict . Dict only support (1,a) tuple with 2 value only then only we can convet into dict

 # print(dict(zip(id,first_name,last_name)))

