#nested list comprehension in nested list

example = [[123],[123],[123]]

nested_comp = [[i for i in range(1,4)] for j in range(3)]
print(nested_comp)