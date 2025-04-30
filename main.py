import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import random
import string
import os

SPECIAL_CHARS = "#$%'^,()*+.:|=@?@/][_`{}\\!;~"

def generate_password():
    length = random.randint(8, 16)      
    categories = [
        string.ascii_letters,
        string.digits,
        SPECIAL_CHARS
    ]
    chosen_categories = random.sample(categories, k=2)
    password_chars = [random.choice(cat) for cat in chosen_categories]
    all_chars = ''.join(categories)
    password_chars += [random.choice(all_chars) for _ in range(length - len(password_chars))]
    random.shuffle(password_chars)
    return ''.join(password_chars)

def save_password(website, email, password):
    if not website or not email or not password:
        messagebox.showwarning("Missing Info", "Please don't leave any fields empty!")
        return
    with open("data.txt", "a") as f:
        f.write(f"{website} | {email} | {password}\n")
    messagebox.showinfo("Success", "Password saved successfully!")
    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Password Manager")
root.config(padx=40, pady=40)

logo_path = os.path.join("images", "logo.png")
if os.path.exists(logo_path):
    logo_img = PhotoImage(file=logo_path)
    canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)
else:
    canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
    canvas.create_text(100, 100, text="Logo Not Found", font=("Arial", 16))
    canvas.grid(row=0, column=1)

website_label = tk.Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = tk.Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = tk.Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@email.com")
password_entry = tk.Entry(width=21)
password_entry.grid(row=3, column=1)

def on_generate_password():
    pwd = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, pwd)

gen_pass_btn = tk.Button(text="Generate Password", command=on_generate_password)
gen_pass_btn.grid(row=3, column=2)

def on_add():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    save_password(website, email, password)

add_btn = tk.Button(text="Add", width=36, command=on_add)
add_btn.grid(row=4, column=1, columnspan=2)

root.mainloop()
