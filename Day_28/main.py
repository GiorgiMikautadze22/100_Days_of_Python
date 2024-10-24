import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global reps

    window.after_cancel(timer)
    checkmark.config(text='')
    timer_label.config(text='Timer', fg=GREEN)
    canvas.itemconfig(text_count_down, text='00:00')

    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer_label.config(text=f'Long Break', fg=PINK)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text=f'Short Break', fg=PINK)
        count_down(short_break_sec)
    else:
        timer_label.config(text=f'Work', fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global timer

    checkmarks = ''

    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(text_count_down, text=f'{count_min}:{count_sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            checkmarks += "✓"
        checkmark.config(text=checkmarks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(bg=YELLOW, pady=50, padx=100)

timer_label = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')

canvas.create_image(100, 112, image=tomato_image)
text_count_down = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', command=reset)
reset_btn.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)


window.mainloop()
