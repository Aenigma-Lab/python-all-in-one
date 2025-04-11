# Python tkinter tutorial
# tk-inter, kinter

# starter code

# import tkinter
import tkinter as tk
from  tkinter import ttk
# window = tkinger.Tk()
window = tk.Tk()
window.title('Application')# Title name



# create Lables
name_label = ttk.Label(window, text='Enter your name : ')
name_label.grid(row=0, column=0, sticky=tk.W) # sticky use for left margin 0
# pack , grid -----> for positon of lable.
name_label.configure(foreground='Blue') # configure the colour for lable



age_lable = ttk.Label(window, text="Enter your age : ")
age_lable.grid(row=1, column=0, sticky=tk.W)
age_lable.configure(foreground='#b388ff')# we can pass custom color also

email_lable = ttk.Label(window, text ="Enter your email: ")
email_lable.grid(row=2, column = 0, sticky=tk.W)

gender_label = ttk.Label(window, text="Your Gender: ")
gender_label.grid(row=3, column=0, sticky=tk.W)

# create entry box for name, age and email

name_var = tk.StringVar()
name_entrybox = ttk.Entry(window, width=16, textvariable= name_var)
name_entrybox.grid(row=0 , column=1)
name_entrybox.focus() # by default cursor will be here


age_var = tk.StringVar()
age_entrybox = ttk.Entry(window, width=16, textvariable= age_var)
age_entrybox.grid(row=1 , column=1)

email_var = tk.StringVar()
email_entrybox = ttk.Entry(window, width=16, textvariable= email_var)
email_entrybox.grid(row=2, column=1)

#create combobox
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(window, width=14, textvariable=gender_var, state='readonly')
gender_combobox['values'] = ('Male','Female','Other')
gender_combobox.current(0) # by defualt set to Male
gender_combobox.grid(row=3, column=1)

# radio button
usertype = tk.StringVar()
radiobtn1 = ttk.Radiobutton(window, text='Student', value='Student', variable = usertype)
radiobtn2 = ttk.Radiobutton(window, text='Teacher', value='Teacher', variable = usertype)
radiobtn1.grid(row=4, column=0)
radiobtn2.grid(row=4, column=1)
ttk.Radiobutton(window, text='Student', value='Student', variable = usertype)

#create check button
checkbtn_var = tk.IntVar()
checkbtn = ttk.Checkbutton(window, text="check for subscribe newsletter.", variable=checkbtn_var)
checkbtn.grid(row=5, columnspan=3)# columnspan here it will use 3 column remain will use only 1 because text is large its change the structure of others

# create button
def action():
    username = name_var.get()
    userage = age_var.get()
    useremail = email_var.get()
    user_gender = gender_var.get()
    user_type = usertype.get()
    if checkbtn_var.get() == 0:
        subscribed = "NO"
    else:
        subscribed = "YES"
    print(f"{username} is {userage} years old  and email is {useremail} gender is {user_gender} and it is {user_type}, subscribed {subscribed}")
    

    with open('user_data.txt','a') as file:
        file.write(f'{username}, {userage}, {useremail} ,{user_gender}, {user_type}, {subscribed}\n')

        # after submitting the value remove all values from entry box.that shold not submit same value again. after submitting the value clear the date from the window
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)

# we can use ttk in button also 
submit_button = tk.Button(window, text ="Submit", command=action)
submit_button.grid(row=8, column=0)
submit_button.configure(foreground='Red')



# widget -----> lable, buttons, radion buttons --- tk, ttk 
# ttk--- is same as tk but better then tk 
window.mainloop() # this will infinite execute 



