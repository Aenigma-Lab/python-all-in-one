# set comprehension 
# it is not use so much in python 
# print square of number form 1 to 10


s = {k**2 for k in range(1,11)}
print(s) # set dont follow sequence so square order will not be in squenece


# print names first characherts using set comprehension

names = ['shubham','aman','gaman','chaman']
first_char = {name[0] for name in names }
print(first_char)