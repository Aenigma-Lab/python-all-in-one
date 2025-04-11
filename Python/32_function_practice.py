#crate a function that take a string(name) and return last character of the string.


name = input("Enter you name: ")
def last_char(name):
    return name[-1]
name_last_char = last_char(name)
# last_char(9)     #TypeError: 'int' object is not subscriptable

print(name_last_char)


#function to check number odd or even
user_input = int(input("Enter number to check odd Even: "))
def odd_even(number):
    if number%2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

odd_even(user_input)