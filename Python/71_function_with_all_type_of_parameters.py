# fuction with all type of parameters
#PADK---->
#P --> Parameters
#A ---> Args
#----> Default Parameters
# ----->Kwargs


def func(name = 'unknown', age = 25):
    print(name)
    print(age)
func()



#Parameteters name shubham and age 25 will override the arguments
# name is unknown and age is 24
def func2(name = 'unknown', age = 24):
    print(name)
    print(age)
func2("Shubham",25)


# if you want to use all type of (4) parameters the order will be

def func3(name, *args, last_name = 'unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)


func3('Shubham',1,2,3, a = 1, b = 2)