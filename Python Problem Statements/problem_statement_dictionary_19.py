#Exercise
#  Define a function that takes a nume(n)

#return a dictionary contaning cube of numbers from 1 to n

# Example
#cube_finder(3)
#{1:1,2:8,3:27}


cube = int(input("Enter number to get cube till that number."))

def cube_finder(cube):
  cube_dict = {}

  for i in range(1,cube+1):
    cube_dict.update({i:i**3})

  print(cube_dict)


cube_finder(cube)



