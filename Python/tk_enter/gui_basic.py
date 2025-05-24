import tkinter

window = tkinter.Tk()
window.title("First App ")
window.minsize(width = 500, height =300)

#Label
name = tkinter.Label(text= "Your name", font=("Arial",24,"bold"))

name.pack(side = "left")

window.mainloop()