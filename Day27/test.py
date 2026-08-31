from tkinter import *
from tkinter import ttk

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") if kw.get("make") is not None else "Nissan"
        self.model = kw.get("model") if kw.get("model") is not None else "GT-R"

    def __repr__(self):
        return f"Make: {self.make}\nModel: {self.model}"

car = Car()
print(car)

my_car = Car(make="Toyota", model="Sienna")
print(my_car)



window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    my_label["text"] = input_field.get()

my_label = ttk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padding= 20)


button = ttk.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)


input_field = ttk.Entry(width=10)
input_field.grid(column=3, row=2)

button2 = ttk.Button(text="New button")
button2.grid(column=2, row=0)







window.mainloop()