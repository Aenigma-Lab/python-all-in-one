# Q: Why do we use dictionaries in Python?
# A: Because lists have limitations in representing complex or real-world data. 
#    Lists do not provide a clear way to label or identify what each element represents, 
#    which can lead to confusion and makes the data less readable and harder to maintain.
#____________________________________________________________________________________________________________________

# Example of using a list to store user data:
user = ['Shubham', 24, ['coco', 'kimi no na wa'], ['awakening', 'fairy tale']]

# In this list, we have the user's name, age, favorite movies, and favorite tunes.
# However, it's not clear what each element in the list represents. 
# Someone reading this code might not know which element is the name, the age, etc.
# This lack of clarity can lead to errors and makes the code difficult to understand and maintain.
#____________________________________________________________________________________________________________________

# A better way to represent this data is by using a dictionary:
# How to create dictionaries
user_dict = {
    'name': 'Shubham',
    'age': 24,
    'favorite_movies': ['coco', 'kimi no na wa'],
    'favorite_tunes': ['awakening', 'fairy tale']
}

# print(user_dict[1]) #------>this will give key error if we try to access dictionary as list

print(f"this is dictionary {user_dict}")
print(type(user_dict))
# In this dictionary, we have clearly labeled each piece of data with a key ('name', 'age', 'favorite_movies', 'favorite_tunes').
# This makes the data much easier to understand and work with.

#____________________________________________________________________________________________________________________
# Q: what are dictionaries 
# A:  Unordered  collection of data in key: value pair.


#____________________________________________________________________________________________________________________

# ----->second method to create dictionary is..

user_1 = dict(name = 'Shubham', age = 25)
print(f"Another method to create dictionary {user_1}")
#____________________________________________________________________________________________________________________

# How to access data from dictionary.
# NOTE-----> There is no indexing because of unordered collection of data. 

#____________________________________________________________________________________________________________________

dic_ex = {
    'last_name' : 'Mishra',
    'age': 24,

          }

# Now accessing the dic_ex with the help of key: value_pair.

print(f"accessing 'dic_ex' variable of dictionary {dic_ex['last_name']}")


#Q: which type of data dictionary can store?
#A: Anything----->number, strings, list, dictionary

# Example ----------->
user_info = {
    'name': 'Abhinav',
    'age' : 24,
    'fav_movies': ['movie1','movie2','movie3'],
    'fav_tunes' : ['tune1','tune2','tune3,','tune4']
}


print(user_info['fav_movies'])

#____________________________________________________________________________________________________________________
# HOW TO ADD DATA TO "EMPTY" DICTIONARY

empty_dic = {}
print(f"empty dictionary {empty_dic}")
empty_dic['emp_name']= 'Mahesh'
empty_dic['emp_salary']= 2514545454
print(f"Here inserting data to empty dictionary {empty_dic}")
