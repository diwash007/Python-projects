from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# sqlite
# db = sqlite3.connect("books.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT OR REPLACE INTO books VALUES(4, '4', 'Diwash Dahal', '9.1')")
# db.commit()

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
db = SQLAlchemy(app)

class Books(db.Model):
	book_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250), unique=True, nullable=False)
	author = db.Column(db.String(250), nullable=False)
	rating = db.Column(db.Float(250), nullable=False)

	def __repr__(self):
		return f"<User {self.title}>"

# SQLAchemy
# db.create_all()
# diwash = Books(book_id=1, title="hello", author="diwash", rating=7.8)
# db.session.add(diwash)
# db.session.commit()

# to_delete = Books.query.get(1)
# db.session.delete(to_delete)
# db.session.commit()


@app.route('/')
def home():
    return render_template('index.html', books=Books.query.all())

@app.route("/add", methods=['GET', 'POST'])
def add():
	if request.method == "POST":
		new_book = Books(title=request.form["name"], author=request.form["author"], rating=request.form["rating"])
		db.session.add(new_book)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('add.html')

@app.route("/edit/<int:bid>?remove=<int:remove>", methods=['GET', 'POST'])
def edit(bid,remove):
	to_update = Books.query.get(bid)
	if request.method == "POST":
		to_update.rating = request.form["rating"]
		db.session.commit()
		return redirect(url_for('home'))
	if remove == 1:
		db.session.delete(to_update)
		db.session.commit()
		return redirect(url_for('home'))
	return render_template('edit.html', bid=bid)

if __name__ == "__main__":
    app.run(debug=True)

