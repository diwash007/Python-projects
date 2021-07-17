from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
	def __init__(self, quiz : QuizBrain):
		self.quiz = quiz
		self.quiz_end = False

		self.window = Tk()
		self.window.title("Quizzler")
		self.window.config(padx=20, pady=20, bg=THEME_COLOR)

		self.canvas = Canvas(width=300, height=250, bg="#fff")
		self.txt = self.canvas.create_text(150, 125, text="text", width=270, font=("Arial", 15, "italic"), fill=THEME_COLOR)
		self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

		self.score_label = Label(text="score: 0", fg="#fff", bg=THEME_COLOR, font=("Arial",12,"bold"))
		self.score_label.grid(row=0, column=1)

		checkimg = PhotoImage(file="images/true.png")
		crossimg = PhotoImage(file="images/false.png")

		self.check_btn = Button(image=checkimg, command=self.right_ans, highlightthickness=0)
		self.check_btn.grid(row=2, column=0)

		self.cross_btn = Button(image=crossimg, command=self.wrong_ans, highlightthickness=0)
		self.cross_btn.grid(row=2, column=1)

		self.get_next_ques()
		self.window.mainloop()

	def get_next_ques(self):
		self.canvas.config(bg="white")
		if self.quiz.still_has_questions():
		    self.score_label.config(text=f"Score: {self.quiz.score}")
		    q_text = self.quiz.next_question()
		    self.canvas.itemconfig(self.txt, text=q_text)
		else:
			q_text = f"GAME OVER\nYour Score: {self.quiz.score}"
			self.canvas.itemconfig(self.txt, text=q_text)
			self.score_label.config(text="")
			self.check_btn.config(state="disabled")
			self.cross_btn.config(state="disabled")

	def right_ans(self):
	    self.give_feedback(self.quiz.check_answer("True"))

	def wrong_ans(self):
	    is_right = self.quiz.check_answer("False")
	    self.give_feedback(is_right)

	def give_feedback(self, is_right):
	    if is_right:
	        self.canvas.config(bg="green")
	    else:
	        self.canvas.config(bg="red")
	    self.window.after(1000, self.get_next_ques)
