# list comprehension
# with the help of list comprehension we cna create of list in one line


#create a list of square from 1 to 10
#using normal method 
square = []
for i in range(1,11):
    square.append(i**2) 
print(f"square using normal method {square}")


#________________________________________________________________
# list of square using list comprehension

comprehen_square = [i**2 for i in range(1,11)]
print(f" print square using list comp {comprehen_square}")

#_________________________________________________________________
# Another example create negative number list 1 to 10 using simple method.
neg_list = []
for i in range(1, 11):
    neg_list.append(-i)
print(f"negative list using simple method {neg_list}")

#__________________________________________________________________
# using list comprehension method 
neg_numb = [-i for i in range(1,11)]
print(f"negative list using list comprehension {neg_list}")

#Quesiton>>> you have name list and that list you have to print first word.

names = ['shubham','saurabh','shashank','kartikey']
first_char = [name[0] for name in names]
print(f"first letter of names {first_char}")