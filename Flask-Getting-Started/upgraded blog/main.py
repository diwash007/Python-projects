from flask import Flask, render_template, request
import requests, smtplib


app = Flask(__name__)

my_mail = 
password = 

blog_url = "https://api.npoint.io/7617aece62c07fee8ada"
data = requests.get(blog_url)
posts = data.json()

def send_email(name, email, phone, msg):
	with smtplib.SMTP("smtp.gmail.com") as con:
		con.starttls()
		con.login(user=my_mail, password=password)
		con.sendmail(
			from_addr="My Clean Blog",
			to_addrs="diwashdahal75@gmail.com",
			msg=f"subject:Message from {name} \n\n Phone: {phone} \n Email: {email} \n {msg}")

@app.route('/')
def home():
	return render_template('index.html', posts=posts)

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
	if request.method == 'POST':
		data = request.form
		email = data['email']
		name = data['name']
		phone = data['phone']
		msg = data['message']
		send_email(name, email, phone, msg)
		return render_template('contact.html', sent=True)
	return render_template('contact.html', sent=False)

@app.route('/post/<int:id>')
def post(id):
	if id >= len(posts):
		return "404 not found"
	else:
		return render_template('post.html', post=posts[id])

if __name__ == "__main__":
	app.run(debug=True)