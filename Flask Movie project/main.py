from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
Bootstrap(app)
db = SQLAlchemy(app)

API_KEY = ""
TMDB_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_URL = "https://api.themoviedb.org/3/movie/"

# classes
class Movies(db.Model):
	_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String, nullable=False)
	year = db.Column(db.Integer, nullable=False)
	description = db.Column(db.String, nullable=False)
	rating = db.Column(db.Float, nullable=True)
	ranking = db.Column(db.Integer, nullable=True)
	review = db.Column(db.String, nullable=True)
	img_url = db.Column(db.String, nullable=False)
db.create_all()

class EditForm(FlaskForm):
	rating = FloatField('Rating: ')
	review = StringField('Review: ')
	submit = SubmitField('Update')

class AddForm(FlaskForm):
	title = StringField("Movie Title: ")
	submit = SubmitField('Add')

# functions
def fetch_movie(title):
	details = {
		'api_key': API_KEY,
		'query': title
	}
	response = requests.get(url=TMDB_URL, params=details)
	data = response.json()
	return render_template('select.html', movies=data["results"])
	

# routes
@app.route("/")
def home():
	movies = Movies.query.order_by(Movies.rating.desc()).all()
	for i in range(len(movies)):
		movies[i].ranking = i + 1
		db.session.commit()
	return render_template("index.html", movies=movies)

@app.route("/edit/<int:id>", methods=['POST','GET'])
def edit(id):
	form = EditForm()
	if request.method == 'POST':
		to_edit = Movies.query.get(id)
		to_edit.rating = form.rating.data
		to_edit.review = form.review.data
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('edit.html', form=form)

@app.route("/delete?id=<int:id>", methods=['GET','POST'])
def delete(id):
	to_delete = Movies.query.get(id)
	db.session.delete(to_delete)
	db.session.commit()
	return redirect(url_for('home'))

@app.route("/add", methods=['POST','GET'])
def add():
	form = AddForm()
	if request.method == 'POST':
		title = form.title.data
		select = fetch_movie(title)
		return select
	return render_template('add.html', form=form)

@app.route("/add_movie/<int:id>")
def add_movie(id):
	response = requests.get(url=f"{MOVIE_URL}{id}?api_key={API_KEY}")
	data = response.json()
	new_movie = Movies(
		title=data['title'],
		year=data['release_date'][:4],
		description=data['overview'],
		img_url=data['poster_path']
		)
	db.session.add(new_movie)
	db.session.commit()
	return redirect(url_for('edit', id=new_movie._id))

if __name__ == '__main__':
    app.run(debug=True)


