# define a generator function
# take one number as argument
# generate a sequence of even numbers from 1 to that number

# ex: 5----->2,4
# 7---->2,4,6

# method 1: 
def even_generator(n):
    for num in range(1, n+1):
        if num%2 == 0:
            yield num

even_num = even_generator(10)
for i in even_num:
    print(i)

print("\n\n\n\n")   


# method 2 

def another_even_generator(num):
    for num in range(2,num+1,2):
        yield num

even_number = another_even_generator(20)
for i in even_number:
    print(i)


print("\n\n\n\n")   
# ---------------------------------------------------------------------------------------------------------------------
# but if i use like this then i can iterate multiple time of that loop:
for i in another_even_generator(6):
    print(i)
print("\n\n\n\n")   

for i in another_even_generator(8):
    print(i)

