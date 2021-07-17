from tkinter import *
from tkinter import messagebox
import pyperclip
import json
from random import randint,choice,shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
	"""Password Generator"""
	letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

	nr_letters = randint(8, 10)
	nr_symbols = randint(2, 4)
	nr_numbers = randint(2, 4)

	pw = [choice(letters) for _ in range(nr_letters)]
	pw += [choice(symbols) for _ in range(nr_symbols)]
	pw += [choice(numbers) for _ in range(nr_numbers)]
	shuffle(pw)

	pass_word = "".join(pw)

	password.delete(0, END)
	password.insert(0, pass_word)
	pyperclip.copy(pass_word)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():

	my_dict = {
		site.get().lower(): {
		"email" : uid.get(),
		"password" : password.get(),
		}
	}

	if site.get()=="" or password.get()=="" or uid.get()=="":
		messagebox.showinfo(title="Oops", message="All fields are mandatory!")
	else:
		try:
			with open("data.json") as f:
				data = json.load(f)
				data.update(my_dict)
		except FileNotFoundError:
			data = my_dict

		with open("data.json", "w") as f:
			json.dump(data, f, indent=4)

		site.delete(0, END)
		password.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_pass():
	try:
		website = site.get().lower()
		with open("data.json") as f:
			data = json.load(f)
			if website in data:
				messagebox.showinfo(title=site.get(), message=f"Username: {data.get(website).get('email')}\nPassword: {data.get(website).get('password')}")
			else:
				messagebox.showinfo(title=site.get(), message="Password not in the file.")
	except:
		messagebox.showinfo(title="Data File Not found", message="Data file doesn't exists!!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

#header
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website: ")
website.grid(column=0, row=1)

user = Label(text="Email/Username: ")
user.grid(column=0, row=2)

passwordLbl = Label(text="Password: ")
passwordLbl.grid(column=0, row=3)

# inputs
site = Entry(width=33)
site.focus()
site.grid(row=1, column=1)

uid = Entry(width=50)
uid.insert(0, "diwashdahal75@gmail.com")
uid.grid(row=2, column=1, columnspan=2)

password = Entry(width=33)
password.grid(row=3, column=1)

# buttons
searchBtn = Button(text="Search", width=15, command=search_pass)
searchBtn.grid(column=2,row=1)

generateBtn = Button(text="Generate Password", command=generate)
generateBtn.grid(column=2, row=3)

addBtn = Button(text="Add",width=36, command=add_pass)
addBtn.grid(column=1, row=4, columnspan=2)

window.mainloop()