#practice for loop
#ask user a number like 12456789

#calculate sum of digits ---------> 1 + 2 + 5 + 6 + 7

total = 0

user_input = input("Enter number")
for i in user_input:
  total = total + int(i) #or total += int(i)

  print(total)

  # or ANOTHER METHOD IS------------

final_value = 0
u_input = input("Enter number for sum: ")
len_u_input = len(u_input)
for i in range(0,len_u_input):
  final_value += int(u_input[i])

print(final_value)

