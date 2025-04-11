# in keyword in sets and for loop

s = {1,'a','b','c'}

if 'a' in s:
    print('present')

# for loop
for elements in s:
    print(elements)#it will not print in order becuse it is unorded collection of items

# we can perform mathematicla operation in sets

#union-----> all set all elements
s1 = {1,2,3}
union_set = s | s1
intersection_set = s & s1
print(union_set)
print(intersection_set)

#intersection---> only common elements