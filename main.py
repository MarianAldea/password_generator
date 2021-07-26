from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_button():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for char in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for char in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for char in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    pass_entry.delete(0, END)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#
def search():
    try:
        with open("my_passwords.json",mode="r") as file:
            data = json.load(file)
            website = web_entry.get()

            try:
                email = data[website]["email"]
                password = data[website]["password"]
                if web_entry.get() in data:
                    messagebox.showinfo(title="Password check", message=f"Your password for {email} is {password}")
                else:
                    messagebox.showwarning(message=f"There is no password matching the {website} ", title="No website found")
            except KeyError:
                messagebox.showwarning(message=f"There is no password matching the {website} website", title="No website found")
            finally:
                pass
    except FileNotFoundError:
            messagebox.showwarning(message="There are no Websites saved yet", title="Error")




def add_button():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    text = website + " " + "|" + email + " " + "|" + password
    new_data = {website:{
                    "email":email,
                    "password":password,
    }
    }

    w_ok = True
    p_ok = True
    if len(website) == 0:
        w_ok = messagebox.askokcancel(title="No website", message=f"You did not type in a Website,"
                                                                  f" are you sure you wish to continue")
    if len(password) == 0:
        p_ok = messagebox.askokcancel(title="No password", message=f"You did not type in a Password, "
                                                                   f"are you sure you wish to continue?")
    if w_ok and p_ok:
        try:
            with open("my_passwords.json", mode="r") as file:
                data = json.load(file)
                data.update(new_data)

        except FileNotFoundError:
            with open("my_passwords.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
                print(new_data)
        else:
            with open("my_passwords.json", mode="w") as file:
                json.dump(data, file, indent=4)
                print(data)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)




web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, columnspan=2)
web_entry.focus()

web_label = Label(text="Website:")
web_label.grid(column=0, row=1,)


email_entry = Entry(width=43)
email_entry.grid(column=1, row=2, columnspan=3)
email_entry.insert(0, "pestic12@gmail.com")

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)


pass_entry = Entry(width=17)
pass_entry.grid(column=1,row=3 )

pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

button_add = Button(text="Add",width=36, command=add_button)
button_add.grid(column=1, row=4, columnspan=2)

button_generate = Button(text="Generate Password", command=random_button)
button_generate.grid(column=2,row=3)

button_search = Button(text="Search", command=search)
button_search.grid(column=3,row=1)



window.mainloop()