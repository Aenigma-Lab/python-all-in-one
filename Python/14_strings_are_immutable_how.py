# In Python, strings are immutable. This means that once a string object is created, it cannot be altered. 
# If you try to modify a string by changing a character or slicing, Python will raise an error because strings do not support item assignment.

# Here’s an example of the error you might encounter:
name = "shubham"
#name[1] = "T"  ######### This will raise TypeError: 'str' object does not support item assignment

# Why Strings are Immutable
# Efficiency: Immutable strings can be stored more efficiently. Since their values cannot change, Python can optimize memory usage and performance by reusing the same string objects.
# Hashability: Immutability allows strings to be used as keys in dictionaries and elements in sets, which require hashable objects.

# Working with Strings
# Although strings cannot be modified directly, you can create new strings based on existing ones. Python provides several methods to work with strings, such as replace(), upper(), lower(), and more.

# Example: Using the replace() Method
# The replace() method creates a new string by replacing occurrences of a specified substring with another substring.
name = "shubham mishra"
new_name = name.replace('s', 't')
print(new_name)  # Output: "thubham"

# Here’s a breakdown of the replace() method:
# name.replace('s', 't'): This returns a new string where all occurrences of the character 's' are replaced with 't'.
# The original string name remains unchanged.

# Example: Using String Methods
# Here are some other common string methods:

# upper(): Converts all characters to uppercase.
name = "shubham"
print(name.upper())  # Output: "SHUBHAM"

# lower(): Converts all characters to lowercase.
name = "SHUBHAM"
print(name.lower())  # Output: "shubham"

# strip(): Removes whitespace from the beginning and end of the string.
name = "  shubham  "
print(name.strip())  # Output: "shubham"

# find(): Returns the index of the first occurrence of a substring (returns -1 if not found).
name = "shubham"
print(name.find('b'))  # Output: 3

# Summary
# Immutability: Strings cannot be changed in place. Any modification creates a new string.
# Replacement: Use methods like replace() to create new strings with changes.
# Other Methods: Explore various string methods for different types of transformations and queries.
