from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_url = "https://api.npoint.io/7617aece62c07fee8ada"
data = requests.get(blog_url)
posts = data.json()

@app.route('/')
def home():
	return render_template('index.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

@app.route('/post/<int:id>')
def post(id):
	if id >= len(posts):
		return "404 not found"
	else:
		return render_template('post.html', post=posts[id])

if __name__ == "__main__":
	app.run(debug=True)