import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import random
import pyperclip
import json

window = tk.Tk()

window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = tk.Canvas(width=200, height=200, highlightthickness=0, bd=0)
my_pass_logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_pass_logo)
canvas.grid(column=1, row=0)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    generated_password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END, generated_password)
    pyperclip.copy(generated_password)

def save_password():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if website_data == "" or email_data == "" or password_data == "":
        messagebox.showerror(title="Empty fields!", message="You can't leave any field empty!")
    else:
        try:
            with open("data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent= 4)
        except json.JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent= 4)
        else:
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
                website_entry.delete(0, tk.END)
                email_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)
                messagebox.showinfo(title="Password saved!", message="Password saved!")


website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = tk.Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = ttk.Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

email_entry = ttk.Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")


password_entry = ttk.Entry()
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = ttk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = ttk.Button(text="Add", command=save_password)
add_button.grid(column=1, row=4, columnspan=2,sticky="EW")


window.mainloop()