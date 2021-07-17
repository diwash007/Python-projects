from turtle import Turtle
FONT = ("Courier", 24, "bold")
ALIGN = "center"

class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.score = 0
		self.high_score = 0
		self.read_high_score()

	def write_score(self):
		self.penup()
		self.hideturtle()
		self.goto(0,250)
		self.clear()
		self.write(f"score: {str(self.score)} \t High score: {str(self.high_score)}", True, ALIGN, FONT)

	def update_score(self):
		self.score += 1

	def reset(self):
		if self.score > int(self.high_score):
			self.high_score = self.score
		self.score = 0
		with open("data.txt", "w") as file:
				file.write(str(self.high_score))

	def read_high_score(self):
		try:
			with open("data.txt") as file:
				self.high_score = file.read()
		except:
			with open("data.txt","w") as file:
				file.write("0")

	# def game_over(self):
	# 	self.goto(0,0)
	# 	self.write("Game Over", True, ALIGN, FONT)