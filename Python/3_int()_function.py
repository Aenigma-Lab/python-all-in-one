

first_number = input("Enter first number " )
second_number = input("Enter second number ")

print(first_number+second_number) #here output will be 22 if u enter 2 and 2 because input always take in string to resolve this problem if you want to add these two number you can use int() function.
print("this is second output")
print()

print(int(first_number)+int(second_number))


# or we can do that this way also
print("this is third output")
print()
sum = int(first_number+second_number)
print(sum)

# again if we want to change the sum in string we can use str() function
# like this we have float() function also
print("Sum of two numbers is " + str(sum))


# Note::::::::::: we can also use int before the input method like
# int(intput("Enter first number"))  //so thi will  take value in int.


num_one = str(4)
num_two = float("5")
num_three = int("33")

print(num_two+num_three)

#Here we can add int and float but the final value wiil be in the float only. but we can not add float and int with string.

