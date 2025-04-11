#using list comprehension find square if number is even and find cube if number is odd.
# 2---> square
# 3----> cube

square_cube = [i**2 if (i%2==0) else i**3 for i in list(range(1,11))]
print(square_cube)