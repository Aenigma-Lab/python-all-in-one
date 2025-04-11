# Fibonacci Series.........
# 0 1 1 2 3 5 8 13 21 34

# 1 ---- 0
# 2 ---- 1
# 3 ---- 1
# 4 ---- 2
# 5 ---- 3
# 6 ---- 5


# first method is ###########################
def febonacci(n):
  a = 0
  b = 1
  if n == 1:
    print(a)
  elif n == 2:
    print(a, b)
  else:
    print(a,b, end=",")
    for i in range(n-2):
      c = a+b 
      a = b
      b = c
      print(b, end=(","))
febonacci(10)


#Another method is ############################
user_input = int(input("Enter fibonacci Series to print."))

a, b = 0, 1

for _ in range(user_input):
  print(a, end = " ")
  print()
  a,b = b, a+b
