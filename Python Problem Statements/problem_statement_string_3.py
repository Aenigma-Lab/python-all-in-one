#take two comma separated input from user
#    1..users name example -"Shubham Misra"
#    2..a single character,- "H"

# output 
# 1..username length
# 2..count the character that user inputed(bonus: make case insensitive count
   
first_name, char = input("Enter your name and comma seprated letter repeaded in name that you wnat to check ").split(",")
first_name_lower = first_name.lower()
char_lower = char.lower()
rem_space_char_lower = char_lower.replace(" ","")
first_name_length = len(first_name)
letter_count = first_name_lower.count(rem_space_char_lower)
print(f"your name length is {first_name_length} and {rem_space_char_lower} repeated {letter_count} times.")

# ANOTHER SHORT METHOD IS LIKE THE BELOW.


# Prompt the user to enter the first name and remove any leading and trailing whitespace
l_name = input("Enter the last_name: ").strip()

# Prompt the user to enter the character to count and remove any leading and trailing whitespace
char = input("Enter the character to count: ").strip()

# Convert both the first name and the character to lowercase to ensure case-insensitive comparison
# Count the occurrences of the character in the first name
character_count = l_name.lower().count(char.lower())

# Print the result, showing how many times the specified character appears in the first name
print(f"Character count is {character_count}")

# Explanation of the Code
# Input Collection:

# input("Enter the first name: ").strip(): Prompts the user to enter a first name, then removes any leading and trailing whitespace from the input.
# input("Enter the character to count: ").strip(): Prompts the user to enter a character to count, then removes any leading and trailing whitespace from the input.
# Processing:

# first_name.lower(): Converts the entire first_name to lowercase to ensure the count is case-insensitive.
# char.lower(): Converts the char to lowercase to ensure the count is case-insensitive.
# .count(char.lower()): Counts the number of occurrences of the lowercase char in the lowercase first_name.
# Output:

# print(f"Character count is {character_count}"): Formats and prints the result, showing how many times the specified character appears in the first_name.
