from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	def __init__(self):

		self.color = "green"
		self.snake_segments = []
		self.create_snake()
		self.head = self.snake_segments[0]
		self.head.color("darkgreen")

	def create_snake(self):
		for i in range(3):
			pos = (-i*20,0)
			self.add_segment(pos)

	def move(self):
		for i in range(len(self.snake_segments)-1,0,-1):
			x = self.snake_segments[i-1].xcor()
			y = self.snake_segments[i-1].ycor()
			self.snake_segments[i].goto(x,y)
		self.head.forward(MOVE_DISTANCE)


	def add_segment(self, position):
		sq = Turtle("square")
		sq.color("darkgreen", self.color)
		sq.penup()
		sq.goto(position)
		self.snake_segments.append(sq)

	def reset(self):
		for sef in self.snake_segments:
			sef.goto(700,700)
		self.snake_segments.clear()
		self.create_snake()
		self.head = self.snake_segments[0]
		self.head.color("darkgreen")

	def grow(self):
		self.add_segment(self.snake_segments[-1].position())

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.setheading(LEFT)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)