#center method
name = 'Shubham'
# **shubham**, 11
#here i have written 9 so my sting length is 7 and when i written 9 1 ,1  star add start and end of my name.
print(name.center(9,"*"))

# if i want 2 2 star both side then
print(name.center(11,"*"))

# problem Statment:
# Take use user input and input length can be anything and add 4, 4 star start and end of the user name.

user_name = input("enter your name ")

user_name_length = len(user_name)
print(user_name_length)
print(user_name.center(user_name_length+8, "*"))

# Or we can write:
print(user_name.center(len(user_name)+8, "@"))