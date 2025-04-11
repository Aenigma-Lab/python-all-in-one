# import pdb module
# module - python file contains usefull class and functions wrote 
# by developer


# According to wikipedia  - Debugging is teh process of finding and resolving 
# defects or problems within a computer program that prevent correct
# correct operation of computer software or a system



# Why debugging
# 1) Our program is not running and causing unexpected errors 
# 2) Our program is working fine but not working the same way we want.


# Steps for debugging 
# 1) set trace
# 2) execute code line by line 

import pdb 
pdb.set_trace()
name = input('Please type your name: ')
age = input('Please type your age: ')
print(f'hello {name }and your age is {age}')

final_age = int(age) + 5
print(f'{name } you will be  {final_age} in next five years.')

