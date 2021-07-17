from turtle import Screen
from bat import Bat
from ball import Ball
from scoreboard import Scoreboard 
import time


s = Screen()

s.title("Pong Game")
s.setup(800, 600)
s.bgcolor("skyblue")
s.tracer(0)

bat = Bat(350, "purple")
rbat = Bat(-350, "red")
ball = Ball()
score = Scoreboard()
score.update_score()


s.listen()
s.onkey(bat.up, "Up")
s.onkey(bat.down, "Down")

s.onkey(rbat.up, "w")
s.onkey(rbat.down, "s")


game_on = True 
top_collide = False
while game_on:
	time.sleep(ball.time_delay)
	s.update()
	ball.move()

	if ball.ycor() > 280 or ball.ycor() < -280:
		ball.bounce_y()


	if ball.distance(bat) < 50 and ball.xcor() > 320 or ball.distance(rbat) < 50 and ball.xcor() < -320:
		ball.bounce_x()

	if ball.xcor() > 380:
		ball.reset_position()
		score.l_score += 1
		score.update_score()
		

	if ball.xcor() < -380:
		ball.reset_position()
		score.r_score += 1
		score.update_score()


s.exitonclick()