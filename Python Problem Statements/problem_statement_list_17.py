#filter odd even 
#define a function

# input take list
#input-----> list -------> [1,2,3,4,5,6,7,8,9]

# Output-------> [1,3,5,7,[2,4,6]]

user_input = [1,2,3,4,5,6,7,8,9]
odd_even_list = []
temp_list = []
def odd_even(user_input):
  for num in user_input:
   if num%2 == 0:
     odd_even_list.append(num)
   else: 
     temp_list.append(num)
  odd_even_list.append(temp_list)
  return odd_even_list

final_list =odd_even(user_input)
print(final_list)


# input take list
#input-----> list -------> [1,2,3,4,5,6,7,8,9]

# Output-------> [1,3,5,7,[2,4,6]]
user_input = [1,2,3,4,5,6,7,8,9]
odd_list = []
even_list = []
def odd_even(user_input):
  for num in user_input:
   if num%2 == 0:
     odd_list.append(num)
   else: 
     even_list.append(num)
  output = [odd_list, even_list]
  return output

final_list =odd_even(user_input)
print(final_list)