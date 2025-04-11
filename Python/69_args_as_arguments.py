# suppose i want to pass a list as argument how to do that

def multiply_nums(*args):
    multiply = 1
    print(args)
    for i in args:
        multiply *=i
    return multiply

num = [1,2,3,4,5]
num1 = (2,3,5) #for tuple
print(multiply_nums(num)) #❌if i pass like this it is wrong becuse it wil not unpack all list elements
print(multiply_nums(*num))# ✅ The * will unpack all the elements

print(multiply_nums(*num1))
