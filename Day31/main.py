import tkinter as tk
import pandas
import random

data = pandas.read_csv("french_words.csv")

BACKGROUND_COLOR = "#B1DDC6"
timer = None

word_index = 0

window = tk.Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)


def new_round():
    global data
    if len(data) == 0:
        canvas.itemconfig(language_label, text= "Done!", fill="black")
        canvas.itemconfig(language_text, text="You've learned everything!", fill="black")
        canvas.itemconfig(flash_card, image=card_front)
        wrong_button.config(state="disabled")
        right_button.config(state="disabled")
    else:
        data = pandas.read_csv("french_words.csv")
        french_side(get_random_word_index())

def count_down(index):
    global timer
    timer = window.after(3000, english_side, index)


def english_side(index):
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(language_text, text=data["English"][index], fill="white")
    canvas.itemconfig(flash_card, image=card_back)
    wrong_button.config(state="normal")
    right_button.config(state="normal")

def french_side(index):
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(language_text, text=data["French"][index], fill="black")
    canvas.itemconfig(flash_card, image=card_front)
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")
    count_down(index)


def right():
    global word_index
    global data
    data = data.drop(word_index)
    data = data.reset_index(drop=True)
    data.to_csv("french_words.csv", index=False)
    new_round()

def wrong():
    new_round()


def get_random_word_index():
    global word_index
    word_index = random.randint(0, len(data)-1)
    return word_index

card_front = tk.PhotoImage(file="card_front.png")
card_back = tk.PhotoImage(file="card_back.png")
right_answer = tk.PhotoImage(file="right.png")
wrong_answer = tk.PhotoImage(file="wrong.png")

canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card = canvas.create_image(400, 263, image= card_front)
canvas.grid(column=0, row=0, columnspan=2)

wrong_button = tk.Button(image=wrong_answer, command=wrong)
wrong_button.config(highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(column=0, row=1)

right_button = tk.Button(image=right_answer, command=right)
right_button.config(highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
right_button.grid(column=1, row=1)

language_label = canvas.create_text(400, 150, fill="black", text="", font=("Ariel", 40, "italic"))
language_text = canvas.create_text(400, 263, fill="black", text="", font=("Ariel", 40, "bold"))

new_round()

window.mainloop()
