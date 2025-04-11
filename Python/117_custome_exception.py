# python custom exception 
# Q --- why  custom exception ?
# A --- To increase the readability of code. 


# example 
class NameToShortError(ValueError):
    pass
def validate(name):
    if len(name) < 8:
        raise NameToShortError('name is too short')

username = input('Enter your name: ')
validate(username)
print(f'hello {username}')