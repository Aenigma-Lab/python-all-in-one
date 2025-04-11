# Cretate your first generator with generator function
# 1.) generator function 

# 10 , print  1 to 10 
# yileld is a keyword so you dont have to write in parenthesis because it's not a function  it means you can write as 'yield i' insted of 'yield(i)' 



def nums(n):
    for i in range(1,n+1):
        yield(i)

numbers = nums(10)

for num in numbers:
    print(num)

for num in numbers:
    print(num)