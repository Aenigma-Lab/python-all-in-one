##############################################
###############################################
# KISS - KEEP IT SIMPLE STUPID.################
###############################################
###############################################



#function inside the function:
# check greatest number

# greater funciton check (a,b) which is greater then whever the output we get then we call the greater and pass the out and also pass the third variable the we get know the greatest function.

# Ex: # greater(a,b) ------> a or b
# greater(a or b, c) -------------> greatest

def greater(a,b):
  if a > b:
    return a
  return b

def greatest(a,b,c):
  max_num =  greater(a,b)
  if max_num < c:
    return c
  
print(greater(10,20))
print(greatest(10,20,30))




# using lambda function################
print((lambda a, b, c: max(a, b, c))(11, 90, 12))
