#define a function which will take list containing numbers as input and return list containin square of every elements

# example
# numbers = [1,2,3,4,5,6]
# square_list(numbers)------>return----->[1,4,9,16]

number_list = list(range(1,11))

square_list =[]
def square_number(number_list):
  for number in number_list:
    square_list.append(number**2)

square_number(number_list)

print(square_list)