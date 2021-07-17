from turtle import Turtle, Screen
import random

tl = []
tcolor = [ 'red', 'blue', 'green' , 'orange', 'yellow', 'purple']

def start_race():
	is_race = True
	while is_race:
		for i in tl:
			if i.xcor() > 230:
				is_race = False
				if i.pencolor() == bet:
					print("You won.")
				else:
					print("You lose")
				print(f"Winning turtle is {i.pencolor()}")
			i.forward(random.randint(1,10))
	s.bye()

def text_write():
	texts = Turtle()
	texts.hideturtle()
	texts.penup()
	texts.goto(0,140)
	texts.write("Press Space to start",False,"center", ("Arial",18,"bold"))

s = Screen()
s.setup(500, 400)
bet = s.textinput("Make a bet", "Which color do you choose?")

for i in range(0,6):
	t = Turtle("turtle")
	t.color(tcolor[i])
	t.penup()
	t.goto(-240,i*40 - 100)
	tl.append(t)

text_write()

s.listen()
s.onkey(start_race, "space")
s.exitonclick()
