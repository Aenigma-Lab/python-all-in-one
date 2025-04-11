#Here are some dictionary methods are.....

# fromkeys method.

d = {'name':'unknown','age':'unknown','hobby': 'unknown'}

# if we want to store same  value in multiple keys then insted of writing above we can write this.Warning

di = dict.fromkeys(['name','age','height'], 'unknown')
print(f"using fromkeys method for same value but diffrent keys {di} ")

#_____________________________________________________________________________________________________________________


# insted of list we can pass the tuple also.

di2 = dict.fromkeys(('name','age','height'),'unknown')
print(f"using tuple insted of list {di2}")

#_____________________________________________________________________________________________________________________


# Using get() method to to access dictionary key value.

di3 = {'name':'Shubham','age':'unknown'}
print(di3.get('name'))
   #if you use the wrong key then it will return 'none'. It will not give any error.

print(f" wring key it will return none it will not give error use it for better error handeling {di3.get('names')}")# wrong key it will written none
#_____________________________________________________________________________________________________________________


# Using get method with if else statemnt.

if di3.get('names'):#here the names is wrong key but still statement will execute
  print('present')
else:
  print('not preset')

  #if NOne -------> fasle,  Elese-------> True


  # Clear method : to clear all data of dictionary

  di3.clear()
  print(f"using clear mehtod clear all the data from dictionary {di3}")
#_____________________________________________________________________________________________________________________
  # copy method : to make a copy of dictionary.

  dictionary = {'address':'mumbai',
                'gender':'male'}

  di4 = dictionary.copy()
  print(f"copying the dictionary {di4}")

  # if you assing the varialbe to dictionary both dictionary will same Ex::::::: di4 = dictionary if u use this the dictionary will same so if you pop andy item from di4 that item will also popped form dictionary but in the copy mehtod it will not pop item to another dictionary. and if you use copy then this will create another same dictionary.


# Original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Assigning the original dictionary to a new variable
assigned_dict = original_dict

# Popping an item from the assigned dictionary
popped_value_assigned = assigned_dict.pop('a')

# Displaying the state after popping from the assigned dictionary
print("After popping from assigned_dict:")
print("original_dict:", original_dict)  # Output: {'b': 2, 'c': 3}
print("assigned_dict:", assigned_dict)    # Output: {'b': 2, 'c': 3}
print("Popped value from assigned_dict:", popped_value_assigned)  # Output: 1

# Resetting the original dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Creating a copy of the original dictionary
copied_dict = original_dict.copy()

# Popping an item from the copied dictionary
popped_value_copied = copied_dict.pop('a')

# Displaying the state after popping from the copied dictionary
print("\nAfter popping from copied_dict:")
print("original_dict:", original_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}
print("copied_dict:", copied_dict)      # Output: {'b': 2, 'c': 3}
print("Popped value from copied_dict:", popped_value_copied)  # Output: 1
