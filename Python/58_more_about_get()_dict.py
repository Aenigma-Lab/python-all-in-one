#more about get method if two keys are same in dictionaries.

user = {'name':'shubham','age':24}

print(f"if key not found in dictionary it will written none but insted of not we want our message  like ' {user.get('names', 'name not found.')}'")#


#if in our dictionary more the one same key then it will count only last one.

info = {'name':'shubham',
        'age': 26,
        'age': 25}

print(f"if two same key consider last one only {info}")