# Problem 1: Extracting Substrings
# Given the string "Programming", extract the substring starting from index 3 to index 7 (inclusive) using slicing.

# Anser 1
print("Programming"[3:8])



# Problem 2: Reversing a Substring
# Given the string "HelloWorld", reverse the substring from index 2 to index 8 and print the result.
print("HelloWorld"[8:1:-1])

# Problem 3: Skipping Characters
# Given the string "PythonProgramming", extract every second character from index 1 to index 15.

print("PythonProgramming"[1:15:2])

# Problem 4: Last Three Characters
# Given the string "DataScience", extract the last three characters of the string using slicing.
print("DataScience"[-3:])

# Problem 5: Palindrome Check
# Given the string "radar", use slicing to check if the string is a palindrome (a string that reads the same forwards and backwards).
str_one = "radar"
reversed_str = (str_one[::-1])
if str_one == reversed_str:
  print(f"{reversed_str} is palindrome")
else:
  print(f"{reversed_str} is not palindorm")
# Problem 6: Middle Three Characters
# Given the string "ArtificialIntelligence", extract the middle three characters. Assume the string length is always odd.
given_str = "ArtificialIntelligence"
str_length = len(given_str)
middle_of_str = str_length//2
middle_three_char = given_str[middle_of_str - 1 : middle_of_str + 2 ]
print(middle_three_char)


# Problem 7: Removing Every Other Character
# Given the string "abcdefgh", create a new string by removing every other character starting from the first character.

# Problem 8: Extract and Reverse Specific Range
# Given the string "TheQuickBrownFox", extract the substring from index 3 to index 12 and reverse it.

# Problem 9: Character Swap
# Given the string "HelloWorld", swap the positions of the characters at indices 2 and 8. Print the modified string.

# Problem 10: Removing First and Last Characters
# Given the string "DataScience", remove the first and last characters of the string using slicing.



#problem :Ask user name and print back user name in reverse order. try to make you progrm in 2 lines usin gstring formatting.

name = input("Enter your name ")
print(f'your names reverse string is "{name[-1::-1]}"')