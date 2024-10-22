from tkinter import *

window = Tk()
window.minsize(width=400, height=300)
window.config(padx=200, pady=150)

def convert_mile_to_km():
    converted_value = round(int(user_input.get()) * 1.609, 2)
    converted_label.config(text=str(converted_value))

user_input = Entry(width=10, font=('Aria', 18, 'normal'))
user_input.insert(END, string='0')
user_input.grid(column=1, row=0)

miles_label = Label(text='Miles', font=('Aria', 18, 'normal'))
miles_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to', font=('Aria', 18, 'normal'))
is_equal_label.grid(column=0, row=1)

converted_label = Label(text='0', font=('Aria', 18, 'normal'))
converted_label.grid(column=1, row=1)

km_label = Label(text='Km', font=('Aria', 18, 'normal'))
km_label.grid(column=2, row=1)

button = Button(text='Calculate', command=convert_mile_to_km)
button.grid(column=1, row=2)

window.mainloop()