from random import choice, randint, shuffle
from tkinter import *
from tkinter import messagebox
import pyperclip

FONT_NAME = "Courier"
EMAIL = "Chrissr85@hotmail.com"
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

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    
    site = website_entry.get()
    uname = username_entry.get()
    pword = password_entry.get()

    if len(pword) == 0 or len(site) == 0:
        print(len(pword))
        print(len(site))
        messagebox.showinfo(title="Warning!", message="Please don't leave any field empty.")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"Thes are the detials entered: \nEmail: {uname} \n"
                                                   f"Password: {pword} \nIs it ok to save?")
        if is_ok:
            with open ("data.txt", "a") as file:
                file.write(f"{site} | {uname} | {pword}\n")
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

website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


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
