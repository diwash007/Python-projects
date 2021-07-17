from turtle import Turtle

class Bat(Turtle):
	def __init__(self, x_pos, bcolor):
		super().__init__()
		self.create_bat(x_pos, bcolor)
		

	def create_bat(self, x_pos, bcolor):
		self.setheading(90)
		self.shape("square")
		self.color(bcolor)
		self.shapesize(1, 5)
		self.penup()
		self.goto(x_pos,0)

	def up(self):
		self.forward(30)

	def down(self):
		self.backward(30)