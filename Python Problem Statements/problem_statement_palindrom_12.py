#Define is_palindrome function that take one word in string as input and return True if it is palindrome else return False:

# Palindorm -    word that reads backwards as forwards

# example 
# is_palindorm("madam") ---------> True
# is_plaindrom("naman") ---------> True
# is_palindrom("horse") ----------> False


#logic (algorithm)

#step 1 -> reverse the string.

#step 2 -> compare reverse sting with original string.


user_input = input("Enter to check Palindrome: ")

def is_palindrome(user_input):
  reverse_string =  user_input[::-1]
  print(reverse_string)
  if reverse_string == user_input:
    return True
  return False
    
  
print(is_palindrome(user_input))

#################################################
# Advance Solution
#################################################

def is_pal(user_input):
  return user_input == user_input[::-1]

print(is_pal(user_input))