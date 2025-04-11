# Guess the number

import random

winning_number = random.randint(1,100)
# print(winning_number)

attempt_counter  = 0

while attempt_counter <= winning_number:
    user_input = int(input("Guess a number between 1 to 100: "))
    attempt_counter+=1

    if user_input == winning_number:
        print(f"You win, and you guessed this number in {attempt_counter} times.")
        break
    elif user_input < winning_number:
        print("too low")
        
    
    else:
        print("too high")





#GUI Based.

# import tkinter as tk
# from PIL import Image, ImageTk
# import pygame
# import requests
# from io import BytesIO
# import random

# # Initialize Pygame mixer
# pygame.mixer.init()

# # Define paths for the sounds and URLs for the GIFs
# sound_paths = {
#     'bark': r'D:\PYTHON_A_TO_Z\dog-bark2.wav',  # Use raw string to handle backslashes
#     'baby': r'D:\PYTHON_A_TO_Z\baby-laughing-04.wav'  # Use raw string to handle backslashes
# }

# gif_urls = {
#     'bark': 'https://media.tenor.com/images/53bb31a8b1ad1d94b5ec78c050a5496b/tenor.gif',  # Direct GIF link
#     'baby': 'https://media.tenor.com/images/8a4e9d5677b9d3fa29f7f6882cfdb165/tenor.gif'  # Direct GIF link
# }

# # Load sound files directly from the local file system
# def load_sound(file_path):
#     try:
#         return pygame.mixer.Sound(file_path)
#     except pygame.error as e:
#         print(f"Error loading sound file {file_path}: {e}")
#         return None

# bark_sound = load_sound(sound_paths['bark'])
# baby_sound = load_sound(sound_paths['baby'])

# # Download and load GIF images
# def load_gif(url):
#     response = requests.get(url)
#     image_data = BytesIO(response.content)
#     return Image.open(image_data)

# def display_gif(gif_image):
#     photo = ImageTk.PhotoImage(gif_image)
#     gif_label.config(image=photo)
#     gif_label.image = photo

# # Generate a random winning number
# winning_number = random.randint(1, 100)

# # Function to handle user input and display images
# def check_guess():
#     try:
#         user_input = int(entry.get())
#         if user_input == winning_number:
#             result_label.config(text=f"You win! You guessed the number {winning_number}.")
#             if baby_sound:
#                 pygame.mixer.Sound.play(baby_sound)
#             display_gif(load_gif(gif_urls['baby']))
#         elif user_input < winning_number:
#             result_label.config(text="Too low! Try again.")
#             if bark_sound:
#                 pygame.mixer.Sound.play(bark_sound)
#             display_gif(load_gif(gif_urls['bark']))
#         else:
#             result_label.config(text="Too high! Try again.")
#             if bark_sound:
#                 pygame.mixer.Sound.play(bark_sound)
#             display_gif(load_gif(gif_urls['bark']))
#     except ValueError:
#         result_label.config(text="Please enter a valid number between 1 and 100.")

# # Set up the Tkinter GUI
# root = tk.Tk()
# root.title("Number Guessing Game")

# # Create widgets
# instruction_label = tk.Label(root, text="Guess a number between 1 and 100:")
# instruction_label.pack()

# entry = tk.Entry(root)
# entry.pack()

# guess_button = tk.Button(root, text="Guess", command=check_guess)
# guess_button.pack()

# result_label = tk.Label(root, text="")
# result_label.pack()

# # Label to display GIF images
# gif_label = tk.Label(root)
# gif_label.pack()

# # Start the Tkinter event loop
# root.mainloop()

