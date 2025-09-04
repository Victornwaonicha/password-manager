import random
from tkinter import messagebox
import pyperclip
from tkinter import *



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

    if website == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please don't leave fields empty!")
    else:
        with open('saved_data.txt', 'a') as file:
            file.write(f"Website: {website} | Email: {email} | Password: {password}\n")
        web_input.delete(0, END)
        email_input.delete(0, END)
        pass_input.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
window.minsize(width=550, height=400)

canvas = Canvas(width=200, height=200)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row=0, column=1)

web_label = Label(text="Website")
web_label.grid(row=1, column=0)

web_input = Entry(width=20)
web_input.grid(row=1, column=1)

email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)

email_input = Entry(width=20)
email_input.grid(row=2, column=1)
web_input.focus()

pass_label = Label(text="Password")
pass_label.grid(row=3, column=0)

pass_input = Entry(width=20, )
pass_input.grid(row=3, column=1)


gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=17, command=save)
add_button.grid(row=4, column=1)



window.mainloop()