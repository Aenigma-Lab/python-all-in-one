# define a list function that take list of words as argument and return list with reverse of every element in that list.

# example
# ['abc','tuv','xyz']--------->['cba','uvt','zyx']



alfa = ['abc', 'tuv', 'xyz']

# Reverse each string in the list
reversed_strings = []
for s in alfa:
    reversed_strings.append(s[::-1])

# Reverse the order of the list


print(reversed_strings)  # Output will be ['zyx', 'vut', 'cba']
