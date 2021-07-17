import turtle
import pandas

FONT = ('Arial', 8, 'normal')
MEDIUM_FONT = ('Arial', 15, 'normal')
BIG_FONT = ('Arial', 20, 'bold')
correct_list = []

class State(turtle.Turtle):
	def __init__(self, x, y, ans):
		super().__init__()
		self.penup()
		self.hideturtle()
		self.goto(x, y)
		self.write(ans, align= "center", font= FONT)

screen = turtle.Screen()
screen.title("Guess US States")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# getting data from file
data = pandas.read_csv("50_states.csv")

# while all the answer are not given
while len(correct_list) < len(data):
	answer = screen.textinput(title= f"{len(correct_list)}/50 States correct", prompt= "What's the state name?\n\nexit - exits the game")
	
	if answer.lower() == "exit":
		missing_states = [n for n in data.state if n not in correct_list]
		new_data = pandas.DataFrame(missing_states)
		new_data.to_csv("missed_states.csv")
		break


	for row in data.state:
		if answer.lower() == row.lower():
			# getting coordinates
			x = int(data[data.state == row].x)
			y= int(data[data.state == row].y)
			# Making new object of State class
			new_state = State(x, y, row)
			correct_list.append(row)

game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.write(f"You answered {len(correct_list)} out of {len(data)} states.", align= "center", font= BIG_FONT)
game_over.goto(0, -20)
game_over.write("Check the missed_states.csv file to learn about missed states.", align= "center", font= MEDIUM_FONT)
screen.exitonclick()