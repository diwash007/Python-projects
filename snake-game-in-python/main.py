from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

s = Screen()
s.setup(600,600)
s.bgcolor("skyblue")
s.title("Snake Game by Diwash007")
s.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


sleep_time = 0.15
game_on = True
while game_on:
	sb.write_score()
	s.update()
	time.sleep(sleep_time)
	snake.move()

	# detecting collision with food
	if snake.head.distance(food) < 18:
		sb.update_score()
		snake.grow()
		food.random_loc()

	# detecting collision with wall
	if snake.head.xcor() > 280 or snake.head.xcor() < -295 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
		sb.reset()
		snake.reset()

	for segment in snake.snake_segments[1:]:
		if snake.head.distance(segment) < 10:
			sb.reset()
			snake.reset()

	if sb.score > 49:
		sleep_time = 0.025	
	elif sb.score > 24:
		sleep_time = 0.05		
	elif sb.score > 9:
		sleep_time = 0.10
	
	

s.exitonclick()