# sum of 1 to 10 :
# like  1 + 2 + 3 + 4 + 5................10
total = 0
for i in range(1,11):
  total+=i
print(total)


#In this example take user input
final_value = 0

user_input = int(input("Enter natural number for addition: "))
for i in range (1,(user_input+1)):
  final_value = final_value+i

print(final_value)