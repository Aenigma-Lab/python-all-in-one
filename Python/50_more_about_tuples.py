#looping in tuples
#tuples with one element

#tuple without parenthesis

# tuple unpacking 

#tuple inside tuple

# some functions that we can use with tuple.
#_________________________________________________________________________________________________________________________
mixed_number = (1,3,4,5.0,6,9.0)

# for loop and tuple

for i in mixed_number:
    print(f"using for loop {i}")
#__________________________________________________________________________________________________________________________
# while loop in tuple

i = 0
while i < len(mixed_number):
    print(f"using while loop {mixed_number[i]}")
    i+=1


#_________________________________________________________________________________________________________________________
# tuple with one element for number.
# so this is int type not tuple type this declaration is wrong for tuple for single element. ❌
nums = (1)
print(f"this is wrong declaration of single tuple element {type(nums)}")

word = ("hello")
print(f"this is also not tuple declare as single string {type(word)}")
#__________________________________________________________________________________________________________________________
# this declaration is correct for single element ✅


single_tuple_dec = (1,)
print(f"this is correct tuple declaration for numbers {type(single_tuple_dec)}")

single_word = ("hello",)
print(f"this is tuple we have to declare single string  word tuple like this {type(single_word)}")






#______________________________________________________________________________________________________________________

# tuple without parenthesis () ✅
names = "shubham","aman","raman","saman","daman"
print(f"tuple without parenthesis {type(names)}")

#_____________________________________________________________________________________________________________________
#tuple unpacking.....(jitti value utna variable) else it will give error ✅

student_names = ('shubham','raman','sumit','andrew')
engineer, singer, dancer, athlete = student_names
print(f"unpacking the values {engineer}")

# this is wrong to unpack tuple    ERROR-------------->(ValueError: too many values to unpack (expected 3)) ❌

# it_professional, doctor, master = student_names
# print(engineer)


# list inside tuple -------✅
# we can not perform operation like add, delete , update element in tuple but with the help of list we can do.
states = ('india',['maharashtra','delhi','punjab','gujarat'])
print(f"here one item is poping so gujarat with removed because pop method remove by default last item {states[1].pop()}")
print(f"here bihar element will append in the lst  give list inside the tuple")
print(states)


# function are we cna use 
# min(), max, sum 

a = [1,2,3,4,5,6]
print(a * 2)