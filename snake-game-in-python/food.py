from turtle import Turtle
import random

class Food(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.7, stretch_wid= 0.7)
		self.color("red")
		self.speed(0)
		self.random_loc()


	def random_loc(self):
		x = random.randint(-280, 280)
		y = random.randint(-280, 245)
		self.goto(x,y)
