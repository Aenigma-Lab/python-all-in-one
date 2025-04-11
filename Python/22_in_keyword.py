# in keyword to check that character or substring present in given STRING or LIST or ARRAY is present or not.

name = "shubham"
if 'a' in name:
  print(f"index position of 'a' is {name.find('a')}") 
else:
  print("not present")



# DETAIL EXPLANATION=================>


# The `in` keyword in Python is used to check for membership within an iterable (like a string, list, tuple, etc.).
# It is a straightforward and efficient way to determine if a character or substring exists within a string or element within a collection.

# Explanation:
# For Strings: The `in` keyword checks if a substring exists within the string.
# For Lists/Tuples: It checks if an element exists in the list or tuple.

# String Example:
name = "shubham"

# Check if 'a' is present in the string `name`
if 'a' in name:
    # If 'a' is present, find its index in the string
    print(f"index position of 'a' is {name.find('a')}")
else:
    # If 'a' is not present, print "not present"
    print("not present")

# Checking Membership:
# 'a' in name evaluates to True if 'a' is found in the string `name`. Otherwise, it returns False.

# Finding Index:
# If 'a' is present, `name.find('a')` returns the index of the first occurrence of 'a' in `name`.
# If 'a' is not found, `find()` returns -1.

# Additional Examples:

# Example 1: Checking Substrings in Strings
text = "hello world"
# Check if the substring 'world' is present in the string `text`
if 'world' in text:
    # If 'world' is present, print that the substring was found
    print("Substring 'world' found")
else:
    # If 'world' is not present, print that the substring was not found
    print("Substring 'world' not found")

# Example 2: Checking Single Characters in Strings
sentence = "Python programming"
# Check if the character 'P' is present in the string `sentence`
if 'P' in sentence:
    # If 'P' is present, print that the character was found
    print("Character 'P' found")
else:
    # If 'P' is not present, print that the character was not found
    print("Character 'P' not found")

# Example 3: Checking Elements in a List
numbers = [1, 2, 3, 4, 5]
# Check if the number 3 is present in the list `numbers`
if 3 in numbers:
    # If 3 is present, print that the number was found in the list
    print("Number 3 is in the list")
else:
    # If 3 is not present, print that the number was not found in the list
    print("Number 3 is not in the list")

# Example 4: Checking Elements in a Tuple
colors = ('red', 'green', 'blue')
# Check if the color 'green' is present in the tuple `colors`
if 'green' in colors:
    # If 'green' is present, print that the color was found in the tuple
    print("Color 'green' is in the tuple")
else:
    # If 'green' is not present, print that the color was not found in the tuple
    print("Color 'green' is not in the tuple")

# Summary:
# Strings: Use `in` to check for substrings or characters.
# Lists/Tuples: Use `in` to check for the presence of elements.
# Find Method: To get the index of a character or substring, use the `.find()` method (returns -1 if not found).
