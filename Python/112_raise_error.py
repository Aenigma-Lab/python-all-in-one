def add(a,b):
    if (type(a) is int and type(b) is int):
        return a+b
    return TypeError('OOps you are passing woring data type to function.')

print(add(2,3))