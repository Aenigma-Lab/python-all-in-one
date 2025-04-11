# tuples data structure
# tuples can store any data type.
# most important tuples are immutable , once tuple is created you can't update 

# data inside tuples

# we use tuple when we know our data is not going to change.


example = ('one','two','three')
#no append, no insert, no pop , no remove

day = ('monday','tuesday') # this type of data will not change.

#__________________________________________________________________________________________________________________________

# tuples are faster then  LIST.

# METHOD WE USING WITH TUPLE ARE: 
#_______________________________________________________________________________________________________________________________________
# count -----> how much times same type of element is present.
# index------> find the index position of element in tuple.
# len() -------> find the length of tuple.
# slicing tuple[]-------> we can slice the tuple element but can not change 

# eg:

print(example[:2])

# but we can not do like this 

example[0] = 'three'
print(example)

