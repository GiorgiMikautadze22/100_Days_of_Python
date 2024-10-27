from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)


email_label = Label(text='Email/Username:')
email_label.grid(row=2, column=0)
email_entry = Entry(width=52)
email_entry.insert(0, 'giorgi.mikautadze2223@gmail.com')
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:')
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
password_button = Button(text='Generate Password')
password_button.grid(row=3, column=2)

add = Button(text='Add', width=44)
add.grid(row=4, column=1, columnspan=2)




window.mainloop()

