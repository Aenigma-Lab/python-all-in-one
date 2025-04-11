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

# I want to update User_pofile.

more_info = {'state': 'Utter Prades', 'hobbies':['coding','hacking','listning song']}


user_profile.update(more_info)

print(f"After updating the dictionary {user_profile}")