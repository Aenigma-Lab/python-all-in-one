# EXERCISE, NUMBER GUESSING GAME

# Make a varible, like winning_number and assign any number to it. 

# Ask use to guess number.

# If user guessed correctly then print "YOU WIN!!!"

# If user didn't guesssed correctly then:
      # if user guessded lower then actual number then print "too low"
      # if user guessed higher then actual number then print "too high"

#  google "how to generate randorm number in python " to generate random number winning game.

import random
winning_number = random.randint(1,20) #Return random integer in range (a, b), including both end points.
user_input = int(input("Enter number to guess 1 to 20 :").strip())

if user_input == winning_number:
  print("HURR!! YOU WON")
elif user_input < winning_number:
  print("too low")
elif user_input > winning_number:
  print("to high")
  
