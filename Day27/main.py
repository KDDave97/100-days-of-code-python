from tkinter import *
from tkinter import ttk

window = Tk()
window.config(pady=10, padx= 10)
window.title("Mile to Km Converter")

def calculate():
    try:
        conversion = float(textbox.get()) * 1.60934
        converted["text"] = round(conversion, 2)
    except ValueError:
        converted["text"] = "Enter a number"

is_equal = Label(text="is equal to")
is_equal.grid(column=0, row= 1)

textbox = ttk.Entry()
textbox.focus()
textbox.grid(column=1, row=0)

miles = Label(text="Miles")
miles.grid(column=2, row=0)

converted = Label(text=" ")
converted.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

calculate_button = ttk.Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)

window.mainloop()