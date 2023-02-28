# Pomodoro app

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
def timer_reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    title.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_text.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break)
        title.config(text="Long break", foreground=RED)
    elif reps % 2 == 0:
        title.config(text="Short break", foreground=PINK)
        count_down(short_break)
    else:
        title.config(text="Work")
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # "✓"

def count_down(count):
    global reps
    seconds = count % 60
    minutes = (count - seconds) // 60
    if seconds < 10:
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    clock_reformat = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=clock_reformat)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        check_mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check_mark += "✓"
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

window.after(1000, )

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# import and create image
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

# create text to go over the image - counter
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=timer_reset, highlightthickness=0)
reset_button.grid(row=2, column=2)

title = Label(text="Timer", background=YELLOW, foreground=GREEN, font=(FONT_NAME, 40, "bold"))
title.grid(row=0, column=1)

check_text = Label(background=YELLOW, foreground=GREEN, font=(FONT_NAME, 20, "bold"))
check_text.grid(row=3, column=1)

window.mainloop()
