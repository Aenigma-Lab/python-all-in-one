# common elements finder function

# deficne a functions which take 2 lists as input and return a list.

# which contains common elements of both list.

# example
# input -----> [1,2,3,8] , [1,2,7,8]

# output -----> [1,2]


list_1 = [1,2,3,8,10]
list_2 = [1,2,7,8,9]

# if(list_1[0]) == (list_2[0]):
#   print(list_1[0])


def common_element(list_1, list_2):
  output = []
  count = 0
  for i in list_1:
      if i in list_2:
         count+=1
         output.append(i)

  return output,count

comm_element = common_element(list_1, list_2)
print(f"common element from list 1 {list_1} and list 2{list_2} is and their count is {comm_element}")