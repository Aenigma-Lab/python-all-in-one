#to remove the spaces in the string we use strip() method. we can remove spaces anywhere from the string.

first_name = "              shubham        "
dots = "............................"
last_name = "     mis       hra           "


# print(first_name+last_name)
#lstrip() method: to remove the space from left_side.
print(first_name.lstrip()+dots) # to remove the left side spaces.
print(first_name.rstrip()+dots) # to remove the right side spaces.
print(first_name.strip()+dots)# to remove the left and right side spaces

#remove the space between the the string like last_name left , right and between spaces.

print(last_name.replace(" ","")+dots)
print(first_name.replace(" ","")+dots+last_name.replace(" ",""))





# Removing Spaces from Strings in Python
# 1. lstrip() Method: Removes spaces from the left side of a string.

# 2. rstrip() Method: Removes spaces from the right side of a string.

# 3. strip() Method: Removes spaces from both the left and right sides of a string.

# 4. replace() Method: Replaces all occurrences of a specified substring with another substring. This can be used to remove all spaces from within the string.

# Here is how these methods work with examples:

# python
# Copy code
# Example strings
first_name = "              shubham        "
dots = "............................"
last_name = "     mis       hra           "

# Print the original first name with spaces
print("Original first_name with spaces:")
print(f"'{first_name}'")

# Remove spaces from the left side using lstrip()
print("\nUsing lstrip() to remove left-side spaces:")
print(f"'{first_name.lstrip()}'{dots}")

# Remove spaces from the right side using rstrip()
print("\nUsing rstrip() to remove right-side spaces:")
print(f"'{first_name.rstrip()}'{dots}")

# Remove spaces from both left and right sides using strip()
print("\nUsing strip() to remove both left and right-side spaces:")
print(f"'{first_name.strip()}'{dots}")

# Remove all spaces within the string using replace()
print("\nRemoving all spaces within the last_name string using replace():")
print(f"'{last_name.replace(' ', '')}'{dots}")

# Remove spaces from both the first_name and last_name and concatenate them
print("\nRemoving spaces from both first_name and last_name and concatenating:")
print(f"'{first_name.replace(' ', '')}{last_name.replace(' ', '')}'{dots}")
# Explanation
# lstrip():

# Removes whitespace from the beginning (left side) of the string.
# Example: first_name.lstrip() removes spaces before "shubham".

# rstrip():

# Removes whitespace from the end (right side) of the string.
# Example: first_name.rstrip() removes spaces after "shubham".

# strip():

# Removes whitespace from both the beginning and end of the string.
# Example: first_name.strip() trims spaces around "shubham".

# replace():

# Replaces all occurrences of a specified substring with another substring.






# The replace() method in Python is used to replace occurrences of a specified substring with another substring. Here's the syntax and a brief explanation:

# Syntax
# python
# Copy code
# string.replace(old, new, count)
# Parameters
# old: The substring you want to replace.
# new: The substring you want to replace old with.
# count (optional): The number of occurrences to replace. If omitted, all occurrences will be replaced.
# Example Usage
# Basic Replacement:

# python
# Copy code
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)  # Output: "Hello Python"
# Removing Substrings:

# python
# Copy code
text = "Hello   World"
new_text = text.replace(" ", "")  # Removes all spaces
print(new_text)  # Output: "HelloWorld"


# Limit Replacement:

# python
# Copy code
text = "abababab"
new_text = text.replace("a", "x", 2)  # Replace only the first 2 occurrences of "a"
print(new_text)  # Output: "xxbababab"
# Summary
# string.replace(' ', ''): This call removes all spaces by replacing them with an empty string ''.
# string.replace('old', 'new'): Replaces all occurrences of 'old' with 'new'.
# string.replace('old', 'new', count): Replaces up to count occurrences of 'old' with 'new'.