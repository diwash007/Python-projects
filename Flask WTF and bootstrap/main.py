from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import *

app = Flask(__name__)
app.secret_key = "hello"
Bootstrap(app)

class LoginForm(FlaskForm):
	email = StringField('Email: ', [validators.InputRequired(), validators.Email()])
	password = PasswordField('Password: ', [validators.InputRequired(), validators.Length(min=8)])
	submit = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == "admin@gmail.com" and form.password.data == "12345678":
			return render_template('success.html')
		else:
			return render_template('denied.html')
	return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)