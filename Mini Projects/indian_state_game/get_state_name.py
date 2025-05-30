import pygame
import csv
import sys
import tkinter as tk
from tkinter import simpledialog
import os
import threading

# -------- CONFIGURATION --------
IMAGE_PATH = "indian_map.png"           # Your map image file
CSV_FILE = "state_coordinates.csv"      # Output CSV file
# --------------------------------

# Create CSV with header if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["state", "x", "y"])

# Initialize Pygame
pygame.init()

# Load the map image
try:
    image = pygame.image.load(IMAGE_PATH)
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Setup the window based on image size
width, height = image.get_width(), image.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click on Map to Record State Coordinates")

# Helper function to run tkinter input safely in a thread
def get_state_name(x, y, callback):
    def ask():
        root = tk.Tk()
        root.withdraw()
        state = simpledialog.askstring("State Input", f"Enter state name for ({x}, {y}):")
        root.destroy()
        callback(state)
    threading.Thread(target=ask).start()

# Main loop
running = True
coordinates = []

def save_state(state):
    if state:
        last_x, last_y = coordinates.pop()  # Get the last stored coordinate
        with open(CSV_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([state.strip(), last_x, last_y])
        print(f"Saved: {state.strip()}, {last_x}, {last_y}")

while running:
    window.blit(image, (0, 0))  # Draw image every frame
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            coordinates.append((x, y))  # Save coordinate temporarily
            get_state_name(x, y, save_state)

pygame.quit()
sys.exit()
