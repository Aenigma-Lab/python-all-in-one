#define a function that take list of strings
#list contaning reverse of every string

#use list comprehension to solve this 

#example 
# l = ['abc','tuv','xyz']
# reverse_string(l)-------->['bac','vut','zyx']

list1 = ['abc','tuv','xyz']

reverse_string = [i[::-1] for i in list1]
print(reverse_string)