# list vs generator
# memory uses , time
# when to use list and when to use generators
import time
# list comprehension ---long time to execute
t1 = time.time()
l = [i**2 for i in range(100000000)] # 10 million
print(time.time()- t1)

# generator comphrension ---- very samll time to execute

t1 = time.time()
l = (i**2 for i in range(1000000000)) # 10 million
print(time.time()- t1)


