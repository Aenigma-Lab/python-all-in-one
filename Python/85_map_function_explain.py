#map function

def square(a):
    return a**2

l = [1,2,3,4]
print((list(map(lambda a : a**2, l))))


# create function like my own map function

def my_map(func, l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list

def my_map2(func,l):
    new_list[]

print(my_map(lambda a: a**2,l))