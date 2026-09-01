import tkinter as tk
from tkinter import ttk


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

window = tk.Tk()


# noinspection bad-argument-type
def reset_timer():
    global reps
    window.after_cancel(timer)
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark_symbol.config(text="")

def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
    else:
        title_label.config(text="Work", fg=GREEN)
        window.attributes('-topmost', 1)
        window.attributes('-topmost', 0)
        count_down(WORK_MIN * 60)


def count_down(count ):
    global timer
    count_minute = count // 60
    count_second = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_second:02}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checkmark_symbol.config(text=f"✔" * (reps//2))


window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

title_label = tk.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
title_label.grid(column=1, row=0)

start_button = ttk.Button(text="Start", command= start_timer)
start_button.grid(column=0, row=2)

reset_button = ttk.Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark_symbol = tk.Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
checkmark_symbol.grid(column=1, row=3)



window.mainloop()
