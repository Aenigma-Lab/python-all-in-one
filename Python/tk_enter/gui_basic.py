import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("First App")
window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

# Entry
user_input = tk.Entry(width=20)
user_input.pack()

# Button click handler
def button_clicked():
    my_text = user_input.get()
    my_label.config(text=my_text)

# Button
button = tk.Button(text="Click Me", command=button_clicked)
button.pack()

# Run the application
window.mainloop()
