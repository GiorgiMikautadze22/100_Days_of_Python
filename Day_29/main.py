from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for sym in range(nr_symbols)]
    password_list += [random.choice(numbers) for num in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()

    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=website, message=f'Email: {data[website]["email"]} \nPassword: {data[website]["password"]}')
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='File not found')
    except KeyError as website:
        messagebox.showinfo(title='Error', message=f'{website} does not exist')

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    email = email_entry.get()
    website = website_entry.get()
    password = password_entry.get()

    new_data = {
        website:{
            'email': email,
            'password': password,
        }
    }

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        validation = messagebox.showinfo(title='Oops', message="Please Don't leave any fields empty")
        return validation

    is_ok = messagebox.askokcancel(title=website, message=f'Check again: \n Email: {email} \n Password: {password}')
    if is_ok:
        # data = f'{website} | {email} | {password} \n'
        # with open("data.txt", mode='a') as file:
        #     file.write(data)

        try:
            #Check if File exists
            with open("data.json", "r") as data_file:
                data = json.load(data_file)

        except FileNotFoundError:
            #If file does not exist create it and dump data
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #If file exists update data and dump the updated data
            data.update(new_data)
            with open("data.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            #No matter what clear user input
            password_entry.delete(0, END)
            website_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=img)
canvas.grid(row=0, column=1)

website_label = Label(text='Website:')
website_label.grid(row=1, column=0)
website_entry = Entry(width=33)
website_entry.focus()
website_search_btn = Button(text='Search', width=14, command=find_password)
website_search_btn.grid(row=1, column=2)
website_entry.grid(row=1, column=1)


email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0, 'giorgi.mikautadze2223@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text='Generate Password', command=generate_password)
password_button.grid(row=3, column=2)

add = Button(text='Add', width=44, command=save_password, )
add.grid(row=4, column=1, columnspan=2)

window.mainloop()

