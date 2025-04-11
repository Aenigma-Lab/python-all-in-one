#List inside list.


matrix  = [[1,2,3],[4,5,6],[7,8,9]] # this is 2D list.


#In this matrix there are 3 items means 3 list.

# How to access a particular value like i want access 5?

print(f" Accessing the Single value  {matrix[1][1]}")

# for printing only list :
for i in matrix:
 print(i)

print(f"another for loop\n\n")


# first for loop print the list element and second for loop print all the list elements.
print("Now printing all the elment inside the list")
for sublist in matrix:
  for i in sublist:
      print(i, end = ( ","))
