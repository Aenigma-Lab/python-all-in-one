# Q::::# Find sum of N natural number input by user and finally after sum print final output.

# sum of n natural numbers

# ask a user for natural number(n)print total from 1 to n


#sum of n natural number:
total = 0
i = 1
 
user_input = int(input("Enter any natural number:").strip())

while i <= user_input:
  total = total+i
  i+=1
print(total)