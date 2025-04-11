# function returning two variable
# how it return in tuple let See 


def fun(num_1, num_2):
    add = num_1 + num_2
    mul = num_1 * num_2

    return add, mul

print(fun(10,12)) #(22,120) it will write both output in tuple like this.

#but if you want output in separate variable then
addition, multiplication = fun(11, 10)
print(addition) #Seprate output
print(multiplication)#Seprate output