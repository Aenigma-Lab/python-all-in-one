#split method and Join method
# it convertthe string to list......
########################################################
user_info = 'shubham 25'.split()
print(f"it split from space and convert string to list {user_info}")

user_anoter_info = "shubham,mishra,25".split(",")
print(f"it split from comma becuse in split() function pass , {user_anoter_info}")
 ########################### OR ###################
# Split MultiVerialbe 
name, age = 'shubham, 25'.split()
print(f"multi veriable with split {name}")
print(f"multiple variable with split {age}")


########################################################

#########################################################Joint method..................
# here alos the rule is same we cna not join int and string like ['shubham',25] this will not join
full_name = ['shubham','mishra']
print(f"join method pass , betweeen {','.join(full_name)}")
print(f"join method  pass space between {' '.join(full_name)}")
