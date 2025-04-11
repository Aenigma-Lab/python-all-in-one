user_profile = {
    'username': 'tech_enthusiast',
    'email': 'tech_enthusiast@example.com',
    'location': 'New York',
    'age': 25,
    'interests': ['programming', 'gaming', 'reading'],
    'join_date': '2022-01-15',
    'is_active': True,
    'skills': ['Python', 'JavaScript', 'SQL'],
    'favorite_foods': ['pizza', 'sushi', 'tacos'],
    'hobbies': ['photography', 'hiking', 'traveling'],
    'projects': ['personal website', 'open-source contributions'],
    'social_media': {
        'twitter': '@tech_enthusiast',
        'github': 'github.com/tech_enthusiast',
        'linkedin': 'linkedin.com/in/tech-enthusiast'
    }
}


# Add and delete data in dictionary.....

# ADD: this will add the new intrests and remove the old intrest in dictionary.
user_profile['interests'] = ['hacking','travelling']
print(user_profile)

# Pop Method: it will remove the value and return the removed value.
print('\nPOP METHOD\n')
popped_item = user_profile.pop('age')# at lest one argement should pass otherwise it will give error.
print(f"removed item using pop is {popped_item}")
print(type(popped_item)) # data type is int becuse age have int value.


# popitem method: if we want to delete randomely key value pair.
print('\n"POPITEM METHOD"\n')
popped_item = user_profile.popitem()
print(f"popped item is {user_profile}")
print(type(popped_item))