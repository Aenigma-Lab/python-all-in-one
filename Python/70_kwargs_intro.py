#kwargs (keyword argument)
# **kwargs (doiuble star operator)

# kwargs as a parameter
# kwargs will print in dictionary where args are print in tuple

def func(**kwargs):
  print(kwargs)
  print(type(kwargs)) # it will give class dict


func(first_name = "Shubham", last_name = "Mishra")


# so if want to print data we use dictionary so will loop in dict like belwo

def fun(**kwargs):
  for i,j in kwargs.items():
    print(f"{i}: {j}")
fun(name = "Shubham", age = 25, gender= "male")




#we can do like this also

def fun1(**kwargs):
  for i,j in kwargs.items():
    print(f"{i}: {j}")

dictionary = {'name' : 'Shubham',
               'age' : 25,
                'gen':'male'}
fun1(**dictionary)



#here kwargs with normal argument

def fun2(hobby, **kwargs):
  print(hobby)
  print(kwargs)
  for key,value in kwargs.items():
    print(f"{key}, {value}")

fun2("hackingcoading",name="shubham",emp_code="1001",company="abcd")