# greatest in three nubmers.


number_1 = int(input("Enter first number."))
number_2 = int(input("Enter second number."))
number_3 = int(input("Enter third number."))

def greater_number(num1, num2, num3):
  if num1 >= num2 and num1 >= num3:
    print(f"{num1} is greater.")
  elif num1 <= num2 and num2 >= num3:
    print(f"{num2} is greater.")
  else:
    print(f"{num3} is greater.")

greater_number(number_1, number_2, number_3)

