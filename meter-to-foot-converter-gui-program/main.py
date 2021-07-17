from tkinter import *

def doit():
	meterfinal = round(float(meter.get())*3.281,3)
	foot.config(text=f"{meterfinal}")

window = Tk()
window.title("meter to Foot converter")
# window.minsize(width=600, height = 500)
window.config(padx= 20, pady =20)

my_label1 = Label(text="is equal to")
my_label1.grid(column=0, row=1)

my_label2 = Label(text="meter")
my_label2.grid(column=2, row=0)

my_label3 = Label(text="Foot")
my_label3.grid(column=2, row=1)

meter = Entry(width=7)
meter.grid(column=1, row=0)
meter.insert(END, string="0")

foot = Label(text="0")
foot.grid(column=1, row=1)

button = Button(text= "Calculate", command = doit)
button.grid(column=1, row=2)

window.mainloop()
