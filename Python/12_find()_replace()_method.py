# replace() method: The replace() method in Python is used to replace occurrences of a specified substring with another substring in a given string. It requires two arguments:


# find() method(): In this mehod we will find the value.


# SYNTEX==>[replace(old, new, how_many_times_in string )]

string = "I am a software developer and I am very rich."
print(string.replace("developer","Engineer"))
print(string.replace("am","was", 2))



#find method(): to get the position of the word or to get the position of the character in the string.
# SYNTAX====>[find('character of word to find', from which postion to search in number)]

print(f'it will starting searching from zero index {string.find("m")}')

print(f'it will start seraching from {string.find("m",4)}')
# So here the condition is that if you dont know the positon of fist "m" but you want to know the postion of second "m" then use this type of logic to get the positon of second , third so on.
first_m_position = string.find("m")
second_m_position = string.find('m',first_m_position+1)
print(f"second 'm' positon is {second_m_position}")

# ======================================================================================================================================================
