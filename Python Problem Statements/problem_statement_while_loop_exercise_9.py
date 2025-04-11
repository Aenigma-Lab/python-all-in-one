# #ask a user for name

# #Example  - Shubham Mishra

# #Print count of each words 

# #output :
#       # s : 2
#       # h : 3        
#       # u : 1
#       # b : 1
#       # a : 2
#       # m : 2
#       # i : 1
#       # r : 1
#       # space : 1

# # Prompt the user for input
# user_name = input("Enter your name to know character repeated in your name: ")

# # Initialize a dictionary to count occurrences of each character
# final_char = {}

# # Count occurrences of each character
# for i in user_name:
#     if i in final_char:
#         final_char[i] += 1
#     else:
#         final_char[i] = 1

# # Print characters and their counts
# for char, count in final_char.items():
#     if char == ' ':
#         char = 'space'  # Replace space with the string 'space' for clarity
#     print(f"{char} : {count}")




#     # BY USING WHILE METHOD.................TO SOLVE THIS PROBLEM.............................................................................................................

#     # Prompt the user for input
# user_name = input("Enter your name to know character repeated in your name: ")

# # Initialize a dictionary to count occurrences of each character
# final_char = {}

# # Initialize an index for the while loop
# index = 0
# user_name_length = len(user_name)

# # Count occurrences of each character
# while index < user_name_length:
#     char = user_name[index]
#     if char in final_char:
#         final_char[char] += 1
#     else:
#         final_char[char] = 1
#     index += 1

# # Print characters and their counts
# for char, count in final_char.items():
#     if char == ' ':
#         char = 'space'  # Replace space with the string 'space' for clarity
#     print(f"{char} : {count}")


# Another method it is by me....................

name = input("enter your name to get all repeted letter count: ")

temp_value = ""
i = 0
while i < len(name):
  if name[i] not in temp_value:
    temp_value += name[i]
    print(f"{name[i]} : {name.count(name[i])}")

  i+=1