# MORE LIST METHODS ARE::::::::::::::::
# :::::::::::::::::::::::::::::::::::::

########################################################

# count()-------------------->it counts how much times the element are in the list.
########################################################
bag =['book','pen','pencil','pen']

print(f"counting the number of occurance of element {bag.count('pen')}")#output: 2



# sort()---------------------->it will short element according to alfabeticla order. it short in our original list.
########################################################

fruits = ["apple","mango","banana","lichi"]

fruits.sort()
print(f"List element arrange in assending order {fruits}")

numbers = [10,15,1,6,19,12,11,5,2,15]
numbers.sort()
print(f"shorting numbers {numbers}")


# shorted function-------------> it also short  element in alfabetical order but original list remain same.
########################################################

number_count = [1,3,4,2,9,8,0,4,7]
print(f"shorted new list {sorted(number_count)}")
print(f"our original list {number_count}")

# reverse---------------------->

# clear------------------------->it will clear the whole list and it print empty list.
######################################################
alfabet = ['a','c','f','g']
alfabet.clear()
print(f"After clearing the list it become empty {alfabet}")

# copy------------------------->it will copy the list
########################################################
numbers_copy = number_count.copy()
print(f"copying the list using coyping function{numbers_copy}")

