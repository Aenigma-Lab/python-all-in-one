#generators

#---> Generators are iterators
# iterator, iterable

# map function already contain iterator. 

l = [1,2,3,4] #iterable

# for i in l:
#     print(i)
i =  iter(l) #this is iterator
print(next(i))
print(next(i))
print(next(i))
print(next(i))

# we can not call like this 
# netxt(l) ----> we can not directly call on iterable
print()
for num in (map(lambda a: a**2, l)):
    print(num)