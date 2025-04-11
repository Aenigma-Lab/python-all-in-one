# take user input and print dictionary like this
# output like this.................
# user = {
#     'name' : 'Shubham',
#     'age' : 25,
#     'fav_movies' : ['installer','avengers'],
#     'fab_songs' : ['song1','song2']
# }

user = {}

name = input('enter your name: ')
age = input('Ente your age: ')
fav_movies = input('Enter your fav movies seprated by comma: ').split(",")
fav_song = input('Enter your fav song seprated by comma: ').split(",")

user['name'] = name
user['age'] = age
user['fav_movies'] = fav_movies
user['fav_song'] = fav_song

for key, value in user.items():
    print(f"{key}: {value}")
  