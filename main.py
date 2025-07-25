from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

FONT_NAME = "Courier"
EMAIL = "INPUT EMAIL HERE"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

def find_password():
    site = website_entry.get()
    try:
        with open("data.json", "r") as file:
            info = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oh Shoot!",
                            message="There is no data file")
    else:
        if site in info:
            email = info[site]["email"]
            password = info[site]["password"]

            messagebox.showinfo(title="Found it!",
                                        message=f"Your email is: {email}\n\n"
                                                f"Your password is: {password}\n")
        else:
            # messagebox.showinfo(title="Sorry",
            #                     message=f"We don't have a password for {site}")
            website_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    site= website_entry.get().title()
    uname = username_entry.get()
    pword = password_entry.get()
    new_data = {site: {
        "email":uname,
        "password": pword,
    }}

    if len(pword) == 0 or len(site) == 0:
        messagebox.showinfo(title="Warning!", message="Please don't leave any field empty.")
    else:
        try:
            with open ("data.json", "r") as file:
                #Reading old data
                info = json.load(file)
        except FileNotFoundError:
            with open ("data.json", "w") as file:
                json.dump(new_data, file, indent= 4)
        else:
            # Updating old data with new data
            info.update(new_data)

            with open ("data.json","w") as file:
                #Saving updated data
                json.dump(info, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website and box
website_label = Label(text="Website:", font=(FONT_NAME, 12,))
website_label.grid(row=1, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

search_button = Button(text= "Search", command=find_password, width=13)
search_button.grid(row=1, column=2)


# Username and box
username_label = Label(text="Email/Username:", font=(FONT_NAME, 12,))
username_label.grid(row=2, column=0)

username_entry = Entry(width=38)
username_entry.grid(row=2, column=1, columnspan=2)
username_entry.insert(0,EMAIL)

# password box and button
password_label = Label(text="Password:", font=(FONT_NAME, 12,))
password_label.grid(row=3, column=0)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = Button(text= "Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

# button
add_button = Button(text= "Add", command=add_password, width=36)
add_button.grid(row=4, column=1,columnspan=2)






window.mainloop()
