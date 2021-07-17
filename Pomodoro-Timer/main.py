from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 0.2
LONG_BREAK_MIN = 0.8
reps =  0
the_timer = None
is_timer_on = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
	window.after_cancel(the_timer)
	global reps
	global is_timer_on
	reps = 0
	is_timer_on = False
	timer.config(text="TIMER", fg=GREEN)
	check_marks.config(text="")
	canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
	global is_timer_on
	if is_timer_on == False:
		is_timer_on = True
		global reps
		reps += 1
		def secs(min):
			return min * 60

		work_sec = secs(WORK_MIN)
		short_break_sec = secs(SHORT_BREAK_MIN)
		long_break_sec = secs(LONG_BREAK_MIN)

		if reps % 8 ==0:
			timer.config(text="BREAK", fg=RED)
			count_down(long_break_sec)
		elif reps % 2 == 0:
			timer.config(text="BREAK", fg=PINK)
			count_down(short_break_sec)
		else:
			timer.config(text="WORK", fg=GREEN)
			count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
	global the_timer
	minute_prefix = ""
	second_prefix = ""
	if count/60 < 10:
		minute_prefix = "0"
	if count%60 < 10:
		second_prefix = "0"

	display_text = f"{minute_prefix}{int(count/60)}:{second_prefix}{int(count%60)}"
	canvas.itemconfig(timer_text, text=display_text)
	if count > 0:
		the_timer = window.after(1000, count_down, count - 1)
	else:
		global is_timer_on
		is_timer_on = False
		start_timer()
		marks = ""
		for _ in range(int(reps/2)):
			marks += "✓"
		check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=103, pady=50, bg=YELLOW)

timer = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

canvas = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=img)
timer_text = canvas.create_text(100, 139, text="01:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1, column=1)

start_btn = Button(text="    Start    ", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="    Reset   ", command=reset_timer)
reset_btn.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW, font=("FONT_NAME", 25, "bold"))
check_marks.grid(column=1, row=3)

window.mainloop()