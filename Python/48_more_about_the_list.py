#genere lists with range functions

#something more about pop method

#index method

#pass list to a function
#_______________________________________________________________________________________________________________________________________

# CREATE LIST USING RANGE FUNCTION

numbers = list(range(1,21))
print(f"My origianl list is {numbers}\n")

# __________________________________________________________________________________________________________________________________________
# USING POP METHOD.(by default it remvoe last element from the list.)
poped_item = numbers.pop()#it will delete last number form list #20
print(poped_item)
# __________________________________________________________________________________________________________________________________________

print(f"After pop() the eleemnt {numbers}\n")

#____________________________________________________________________________________________________________________________________________
# USING INDEX METHOD.....

print(f"Here element '5' present index number {numbers.index(5)}\n")# here 2 is the element which is present on index number 

#___________________________________________________________________________________________________________________________________________
# i want to  find the 1 index position but not the 0th index of 1.
my_number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 11, 17 ,18, 19]

print(f"First position of element 1 index is {my_number_list.index(1)}\n")

print(f"Another element 1 in my list index position is {my_number_list.index(1, 1, 12)} \n")#stop serching element at index 12.


#_________________________________________________________________________________________________________________________________________
# CREATE NEGATIVE LIST:
my_list= list(range(1,11))
print(my_list)
final_list = []
def negative_list(my_list):
  for i in my_list:
    final_list.append(-i)

negative_list(my_list)

print(final_list)
