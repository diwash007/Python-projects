from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------- Getting data ------- #
try:
	data = pandas.read_csv("data/words_to_learn.csv")
except:
	data = pandas.read_csv("data/french_words.csv")
data_list = data.to_dict(orient="records")
current_card = {}

# ------- FUNCTIONS ------- #
def next_card():
	global current_card, flip_timer
	window.after_cancel(flip_timer)
	current_card = random.choice(data_list)
	canvas.itemconfig(title, text="French", fill="black")
	canvas.itemconfig(text, text=current_card["French"], fill="black")
	canvas.itemconfig(img, image=front)
	flip_timer = window.after(3000, flip)

def flip():
	canvas.itemconfig(title, text="English", fill="white")
	canvas.itemconfig(text, text=current_card["English"], fill="white")
	canvas.itemconfig(img, image=back)

def is_known():
	data_list.remove(current_card)
	df = pandas.DataFrame(data_list)
	df.to_csv("data/words_to_learn.csv", index=False)
	next_card()

# ------- UI SETUP ------- #
window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

# card images
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

# card
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
img = canvas.create_image(400, 263)
title = canvas.create_text(400, 150, font=("Arial",40,"italic"))
text = canvas.create_text(400, 263, font=("Arial",60,"bold"))
canvas.grid(row=0, column=0, columnspan=2)

# buttons
cross = PhotoImage(file="images/wrong.png",)
wrong = Button(image=cross, highlightthickness=0, command=next_card)
wrong.grid(column=0, row=1)

check = PhotoImage(file="images/right.png")
right = Button(image=check, highlightthickness=0, command=is_known)
right.grid(column=1, row=1)

next_card()
window.mainloop()