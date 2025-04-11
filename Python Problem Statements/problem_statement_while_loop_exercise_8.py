#problem
#Ask user to input a number containing more than one digit 
# example - 1256
# calculate 1+2+5+6 and print

# algorithm - (method to solve problem in human language)
# ask input in string , ie. dont change string to int
#example - '123435'
#pick string character one by one and change to int
#int(example[0] + int(example[1] ------ go up to len(example))


user_input = input("Enter number to add like ::  ")

user_input_len = len(user_input)
print(f"user input length is {user_input_len}")

i = 0
total = 0
while i < user_input_len:
  total = total+(int(user_input[i]))
  i+=1
print(f"sum of natural number is {total}")