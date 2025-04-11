#default parameters
# "unknown", "none"    is default parameter it should pass in last only otherwirse it will give error.

# unknown = Default 
# None  = Kuch bee nahi(nothing)




# Another Method is : this is also correct
def user_info_2(first_name, last_name=None, age=25):
  print(f"your first name is {first_name}")
  print(f"your last name is {last_name}")
  print(f"your age is  {age}")

user_info_2("Shubham","mishra")



# another type is  # this is right 
def user_info_2(first_name, last_name= "unknown", age=None):
  print(f"your first name is {first_name}")
  print(f"your last name is {last_name}")
  print(f"your age is  {age}")

user_info_2("Shubham", 24)




# another type is  # this is right 
def user_info_4(first_name, last_name= "unknown", age="unknown"):
  print(f"your first name is {first_name}")
  print(f"your last name is {last_name}")
  print(f"your age is  {age}")

user_info_4("Alfa", 399)

# This will wrong becuse default parament should in last.

# def user_info_1(first_name, last_name= "unknown", age):
#   print(f"your first name is {first_name}")
#   print(f"your last name is {last_name}")
#   print(f"your age is  {age}")

# user_info_1("Shubham", 24)


# Another Method is : this is also correct
# passed parameters are user_info_3(default, defualt, kuch bee nahi)
def user_info_3(first_name="unknown", last_name="unknown", age=None):
  print(f"your first name is {first_name}")
  print(f"your last name is {last_name}")
  print(f"your age is  {age}")

user_info_3()






print(f"\n\n-----------------------------------------\nbreak \n-----------------------------------------")


# Rules for Passing Arguments

# Positional Arguments:
# Definition: Arguments that must be passed to a function in the exact order they are defined.
# Usage: Always specify values for positional parameters in the order they appear in the function definition.
# Example:
def example(a, b):
    print(a, b)

# Calling with positional arguments: 1 is assigned to a, 2 is assigned to b
example(1, 2)  # Output: 1 2

# Keyword Arguments:
# Definition: Arguments passed by explicitly specifying the parameter names.
# Usage: You can specify arguments in any order if you use the parameter names.
# Example:
def example(a, b):
    print(a, b)

# Calling with keyword arguments: b is assigned to 2, a is assigned to 1
example(b=2, a=1)  # Output: 1 2

# Default Parameters:
# Definition: Parameters that have default values specified in the function definition.
# Usage: If the caller does not provide a value for these parameters, the default value is used.
# Example:
def example(a, b=5):
    print(a, b)

# Calling with only one argument: b defaults to 5
example(1)  # Output: 1 5

# Optional Parameters:
# Definition: Parameters that are not required; they have default values.
# Usage: Can be omitted when calling the function, in which case the default value is used.
# Example:
def example(a, b=None):
    print(a, b)

# Calling with only one argument: b defaults to None
example(1)  # Output: 1 None

# Calling with both arguments provided: b is set to 2
example(1, 2)  # Output: 1 2

# Explicit None for Optional Parameters:
# Definition: None can be passed explicitly as a value to indicate the absence of a meaningful value.
# Usage: Useful to differentiate between no value being provided and a specific value of None.
# Example:
def example(a, b=None):
    print(a, b)

# Calling with explicit None: b is explicitly set to None
example(1, None)  # Output: 1 None

# Summary of Function Argument Rules
# - Positional Arguments: Must be provided in the order defined.
# - Keyword Arguments: Can be specified in any order using parameter names.
# - Default Parameters: Have a default value if not provided.
# - Optional Parameters: Can be omitted; defaults to the specified default value.
# - Explicit None: Use None to signify that no specific value is provided for an optional parameter.
