from art import logo, vs
from game_data import data
import random


print(logo)

score_count = 0
def random_game_data():
    return random.choice(data)

# print(random_game_data())

def game_data_format(account):
    return f"{account['name']} is a {account['description']} and country is  {account['country']} and total follower is {account['follower_count']}"


a = random_game_data()
b = random_game_data()


while a == b:
    b = random_game_data()

# Game loop
while True:
    print(f"Compare A: {game_data_format(a)}")
    print(vs)
    print(f"Compare B: {game_data_format(b)}")
    
    
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    # Check for invalid input
    if choice not in ['a', 'b']:
        print("Invalid choice! Please type 'A' or 'B'.")
        continue  

    
    if (choice == 'a' and a['follower_count'] > b['follower_count']) or (choice == 'b' and a['follower_count'] < b['follower_count']):
        score_count += 1
        print(f"You are right! Current score: {score_count}") 
        
        # updating account for next round
        a = b
        b = random_game_data()
        
        #ensure  a and b both not same
        while a == b:
            b = random_game_data()
    else:
        print(f'your final score is {score_count}')
        break
        