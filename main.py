import random
from json import JSONDecodeError
from tkinter import messagebox
import pyperclip
from tkinter import *
import json

RED = "#FF0000"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    lower_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                  "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    upper_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "H", "J", "K", "L",
                  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    letters = lower_list + upper_list

    digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    sym_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+', "-", "_",]

    random_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    random_digit = [random.choice(digit_list) for _ in range(random.randint(2, 4))]
    random_symbols = [random.choice(sym_list) for _ in range(random.randint(2, 4))]

    password_list = random_letters + random_digit + random_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    # clear old text
    pass_input.delete(0, END)

    # insert new password
    pass_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            'email': email,
            'password': password,
        }
    }

    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the info entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs is okay to save now?")

        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # Reading data
                    data = json.load(data_file)
                    # Updating data
                    data.update(new_data)

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # Saving new data for the first time
                    json.dump(new_data, data_file, indent=4)

            else:
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                web_input.delete(0, END)
                # email_input.delete(0, END)
                pass_input.delete(0, END)
                messagebox.showinfo(title="Success", message="Thank you!!")


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = web_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No File Found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showwarning(title="Error", message=f"{website} Details Not Found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# window.minsize(width=550, height=400)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

web_input = Entry(width=21)
web_input.grid(row=1, column=1)
web_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "mallo@mmm.com")

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=35)
pass_input.grid(row=3, column=1, columnspan=2)


search_button = Button(text="Search", width=12, command=find_password, font=("Arial", 12), fg=RED)
search_button.grid(row=1, column=2)

gen_pass = Button(text="Generate Password", command=generate_password, width=12, font=("Arial", 12), fg=RED)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=save, fg=RED)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()



