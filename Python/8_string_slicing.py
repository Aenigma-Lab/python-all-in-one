#string slicing / or selecting sub sequences.

# if you want to cut any part of the string that is called string slicing or or sub sequences.

language = "python"
print(language[4]) #here will get one characer of the string but if we want more then one charachter then.

# SYNTAX ======> [START ARGUMENT : STOP ARGUMENT-1]
# start argument = starting point of string.
# stop argument =  ending point of the string.


print(f"here we want to print only 'py'. {language[0:2]}") 

print(f"Here we want to print 'th'. {language[2:4]} ")

# we can also use the negative indexing to print strings
print(f"Here we want to print 'ho' with using negative indexing. {language[-3:5]}")

#if we dont pass any argument then it will print whole string.
print(f"Here it will give whole string without passing assing any argument. {language[:]}") 

# suppose we not pass only the start and only end argemnt how it will work.
print(f"not passed the end argument in string.  {language[1:]}")

print(f"not passed the start argument in the string.  {language[:4]}")


print("Shubham"[3:-6:-1])