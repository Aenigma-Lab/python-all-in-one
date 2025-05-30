import pygame
import csv
import sys
import tkinter as tk
from tkinter import ttk
import os
import threading
import pandas as pd

# -------- CONFIGURATION --------
IMAGE_PATH = "indian_map.png"
OUTPUT_CSV = "state_coordinates.csv"
INPUT_CSV = "available_states.csv"
FONT_SIZE = 14
FONT_COLOR = (255, 0, 0)  # Red
# --------------------------------

# Load available state names
try:
    state_df = pd.read_csv(INPUT_CSV)
    available_states = sorted(state_df['state'].dropna().unique().tolist())
except Exception as e:
    print(f"Error loading available states: {e}")
    sys.exit()

# Create output CSV with header if not exists
if not os.path.exists(OUTPUT_CSV):
    with open(OUTPUT_CSV, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["state", "x", "y"])

# Initialize Pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont('Arial', FONT_SIZE)

# Load image
try:
    image = pygame.image.load(IMAGE_PATH)
except pygame.error as e:
    print(f"Error loading image: {e}")
    sys.exit()

# Setup Pygame window
width, height = image.get_width(), image.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Click on Map to Select State and Save Coordinates")

# Store clicked states to draw
drawn_states = []

coordinates = []

def save_state(state):
    if state:
        last_x, last_y = coordinates.pop()
        drawn_states.append((state.strip(), last_x, last_y))  # store for redraw
        with open(OUTPUT_CSV, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([state.strip(), last_x, last_y])
        print(f"Saved: {state.strip()}, {last_x}, {last_y}")

# Dropdown popup in separate thread
def get_state_from_list(x, y, callback):
    def ask():
        def on_submit():
            selected = combo.get()
            if selected:
                root.destroy()
                callback(selected)

        root = tk.Tk()
        root.title(f"Select state for ({x}, {y})")
        root.geometry("300x100")
        root.resizable(False, False)

        tk.Label(root, text="Choose state:").pack(pady=(10, 0))

        combo = ttk.Combobox(root, values=available_states, state="readonly")
        combo.pack(pady=5)
        combo.set("Select State")

        submit_btn = tk.Button(root, text="Submit", command=on_submit)
        submit_btn.pack(pady=5)

        root.mainloop()

    threading.Thread(target=ask).start()

# Main Pygame loop
running = True
while running:
    window.blit(image, (0, 0))  # redraw base image

    # Draw previously added state labels
    for state, x, y in drawn_states:
        label = font.render(state, True, FONT_COLOR)
        window.blit(label, (x, y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            coordinates.append((x, y))
            get_state_from_list(x, y, save_state)

pygame.quit()
sys.exit()
