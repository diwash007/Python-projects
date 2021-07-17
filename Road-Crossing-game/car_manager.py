from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
	def __init__(self):
		self.cars = []
		self.speed = STARTING_MOVE_DISTANCE
		
	def create_car(self):
		new_car = Turtle()
		new_car.shape("square")
		new_car.setheading(180)
		new_car.shapesize(1,2)
		new_car.color(random.choice(COLORS))
		new_car.penup()
		new_car.goto(300, random.randint(-250, 250))
		self.cars.append(new_car)


	def move(self):
		for car in self.cars:
			car.forward(self.speed)
		
	def update_speed(self):
		self.speed += MOVE_INCREMENT

