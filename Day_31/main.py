from tkinter import *
import pandas
import random

from pandas.core.interchange.dataframe_protocol import DataFrame

BACKGROUND_COLOR = "#B1DDC6"

#------------------ Read Data ----------------------------------
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
    print('gela')
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dict = data.to_dict(orient='records')

random_word = {}

def next_card():
    global random_word,flip_timer

    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    canvas.itemconfig(current_img, image=img_front)
    canvas.itemconfig(language_title, text="French",fill='black')
    canvas.itemconfig(word, text=random_word['French'], fill='black')
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(current_img, image=img_back)
    canvas.itemconfig(language_title, fill='white', text="English")
    canvas.itemconfig(word, fill='white', text=random_word['English'])


def is_known():
    data_dict.remove(random_word)
    df = pandas.DataFrame(data_dict)

    df.to_csv("./data/words_to_learn.csv", index=False)

    next_card()

#------------------ UI -----------------------------------------

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
flip_timer =  window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
current_img = canvas.create_image(400, 263, image=img_front)

language_title = canvas.create_text(400, 150, text="gela", font=('Ariel', 40, 'italic'))
word = canvas.create_text(400, 263, text="gocha", font=('Ariel', 60, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="./images/wrong.png")
red_button = Button(image=wrong_image,highlightthickness=0, command=next_card)
red_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
green_button = Button(image=right_image,highlightthickness=0, command=is_known)
green_button.grid(row=1, column=1)

next_card()

window.mainloop()