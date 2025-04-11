# In keyword and iterations in dictionary

user_info = {
  'name' : 'Shubham',
  'age' : 25,
  'fav_movies' : ['coco','kimi no na wa'],
  'fav_song' : ['awakening','fairy tale']
}

# check if key exist in dictionary

if 'age' in user_info:
  print('Key exist in dictionary.')
else:
  print("Key not present in dictionary")

#_____________________________________________________________________________________________________________________

# Check if values exist in dictionary-----------> Value method

if 'shubham' in user_info.values():
  print('Value present in Dictionary')
else:
  print('Value not present in dictionary')

  #______________________________________________________________________________________
if '25' in user_info.values(): # wrong becuse 25 is int and we have taken string.
  print('Value Present')
else:
  print('Value not present.')

#_____________________________________________________________________________________________________________________

# Loop in dictionaries.

#__________________________________________________________
# This will Print all the keys.....
print('start looping keys\n')
for i in user_info:
  print(i)

print('\n')
#_____________________________________________________________________________________________________________________

# This will print all the values.......

print('start printing values\n')
for i in user_info.values():
  print(i)


# value method : i having all the values we iterate it

user_info_values = user_info.values()
print(f'it type is {type(user_info_values)} and {user_info_values} but is is not list we can not perfom operation like add delete but we can iterate through dic values')


# keys method : i having all the keys we can iterate it
user_info_keys = user_info.keys()
print(user_info_keys)
print(type(user_info_keys))

# This loop will print all the vlues......
print('\nanother method to print all keys\n')
for i in user_info:
  print(user_info[i])

# Items method
user_items = user_info.items()
print('\nthis will return key value in tuple format\n')
print(user_items)
print(type(user_items))

# How usefull this item method to help printing key value.
for key, value in user_info.items():# insted of key value we can use another variable for example i, j
  print(f'Key is {key} and value is {value}')


# What if i use only one variable. so it will print the tuple format. like (key, value)

for i in user_info.items():
  print(i)
