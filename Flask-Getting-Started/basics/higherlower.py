from flask import Flask
import random
app = Flask(__name__)

goal = 0

@app.route('/')
def home():
	global goal
	goal = random.randint(0,10)
	return "<h1><br>Guess a no. between 1 and 10</h1>"\
			"<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

@app.route('/<int:num>')
def check(num):
	if num == goal:
		return("Correct")
	elif num < goal:
		return("Too low")
	else:
		return("Too high")

if __name__ == "__main__":
	app.run(debug=True)