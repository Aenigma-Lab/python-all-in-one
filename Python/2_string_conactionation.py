# if both varibale contain string then string can be concatinate but string and number can not be concatinate but still you want to concatinate with number then you have to convert  number to string then you can concatinate number and string.

first_name = "precihole"
last_name = "sports"
print(first_name +" "+ last_name)

# print(first_name+3) ///TypeError: can only concatenate str (not "int") to str

#to fix this issue we can do like this 
print(first_name+"3")
print(first_name+str(3))

#we can not concatnat the string with number but we can multiply the string with number like below

print(first_name " " * 3) #so this will print 3 times.