# what is string formating?
# if we want to print some  output there are multiple method we can use to print output using string formating.
# we will study only python3 and python3.6 string formating.

name = "Shubham"
age  = 25

print("hello "+ name + " you age is " +str(age)) #so this is ugly  syntax we dont use this 

# string formating in python 3 is below like this here we use the format() function. here not to worry about you data in string or int format it automaticlly handle the data type and give you the proper output.
print("hello {0} your age is {1} ".format(name,age)) #python 3 syntax

#In python 3.6 string formating become more simple and proper just use print(f"{} {}") before the double quotation. and pass you variable in curly braces, it will automatically handle the int, sting , float dobule, all types of the data.
print(f"your name is {name} and your age is {age} ") #python 3.6 clean format.

