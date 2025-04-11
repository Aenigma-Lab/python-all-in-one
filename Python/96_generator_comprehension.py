# generatator Comprehension 

# insted of using [] bracket use () to make generator in list comprehension 
# this is list comprehension 
list_square = [i**2 for i in range(1,11)]
print(list_square)



print("\n\n\n\n")
# this is generator comphrension 

generator_square = (i**2 for i in range(1,20))
print(generator_square)# this is generator object.------

for i in generator_square:
    print(i)

for j in generator_square:
    print(j)