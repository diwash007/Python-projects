from turtle import Turtle 
FONT = ("Courier", 22, "bold")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.level = 1
		self.write_score()

	def write_score(self):
		self.penup()
		self.hideturtle()
		self.goto(-220, 265)
		self.write("Level: " + str(self.level), True, "center", FONT)

	def update_score(self):
		self.level += 1
		self.clear()
		self.write_score()