#what is scope of varialbe.

x =  5 #this is not local variable, it is outside the function.
def fun():
  global x #this x is global x outside the function.
  x = 7 # this is the local variable we can not use this varibale outside of fun() function.
  return x
print(x)
print(fun())

print(x)  #5              # we can not print x here becuase while pringting x it is outside the function.

