from flask import Flask, render_template
import random
import requests
from datetime import datetime
app = Flask(__name__)

def find_details(name):
	response1 = requests.get(f'https://api.agify.io/?name={name}')
	response2 = requests.get(f'https://api.genderize.io/?name={name}')

	age_data = response1.json()
	gender_data = response2.json()

	age = age_data['age']
	gender = gender_data['gender']

	return (age, gender)

@app.route('/')
def home():
	rand_num = random.randint(1,10)
	date = datetime.today().strftime('%Y')
	return render_template('index.html', num=rand_num, f=date)

@app.route('/guess/<name>')
def detail(name):
	age, gender = find_details(name)
	return render_template('details.html',name=name,age=age,gender=gender)

@app.route('/blog')
def blog():
	blog_url = "https://api.npoint.io/7617aece62c07fee8ada"
	data = requests.get(blog_url)
	posts = data.json()
	return render_template('blog.html',posts=posts)


if __name__ == '__main__':
	app.run(debug=True)