from turtle import Turtle
import random
color = ["orange", "darkred", "green", "brown", "black"]

class Ball(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.color(random.choice(color))
		self.setheading(45)
		self.penup()
		self.x_move = 10
		self.y_move = 10
		self.time_delay = 0.1


	def move(self):
		self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

	def bounce_y(self):
		self.y_move *= -1

	def bounce_x(self):
		self.x_move *= -1
		self.time_delay *= 0.9

	def reset_position(self):
		self.goto(0, 0)
		self.time_delay = 0.1
		self.x_move *= -1

