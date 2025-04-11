# Task: Define a Function

# Description
# You need to define a function named `to_power` that takes a number 
# and an iterable (such as a list or tuple) containing numbers as arguments. 
# The function should raise each number in the iterable to the power of the given number.

# Requirements
# - If the user does not pass any arguments (other than the first number), 
#   the function should return a message: "Hey, you didn't pass any args."
# - If arguments are provided, the function should return a list containing 
#   each number raised to the power of the given number.

# Example
# If `nums = [1, 2, 3]` and you call `to_power(3, *nums)`, the output should be:
# [1**3, 2**3, 3**3] => [1, 8, 27]

# Note
# - Use list comprehension to generate the resulting list.

# Function Signature
# def to_power(exp: int, *args: int) -> list:
#     pass


def to_power(power, *args):
  if not args:
    return "Hey, you did not pass any arguments"

  result = [i ** power for i in args]
  return result
    
  

num_list = input('Enter a list of numbers to find the power, separated by commas: ')
if num_list.strip():  # Check if the input is not just whitespace
    num_list = [int(num) for num in num_list.split(',')]
else:
    num_list = []  # If no numbers were entered, set to empty list

power = (input("Enter number for power: "))

#check if power input is empty
if not power.strip():
  print("you did not enter a power and *args")
else:
  power = int(power)
  if num_list:
    print(to_power(power, *num_list))
  else:
    print("Hey you did not pass any argumets.")