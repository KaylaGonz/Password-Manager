import random
import json
import pyperclip
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(1, 3)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:

        try:
            with open("data.json", mode="r") as file:
                # json.dump(new_data, file, indent=4)   # how to write to json
                data = json.load(file)      # how to read json file, data is loaded into a dictionary "data =", reading old data
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)

        else:
            data.update(new_data)       # update the "data" dictionary with "new_data"

            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  # saving updated data

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PW -----------------------

def find_password():
    website = website_entry.get()

    try:
        with open("data.json") as file:
            # json.dump(new_data, file, indent=4)   # how to write to json
            data = json.load(file)  # how to read json file, data is loaded into a dictionary "data =", reading old data

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=("Ariel", 10, "bold"))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:", font=("Ariel", 10, "bold"))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=("Ariel", 10, "bold"))
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=20)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_entry = Entry(width=25)
email_entry.grid(column=1, row=2)
email_entry.insert(0, "sample@gmail.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()