from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all()

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('secrets'))
    return render_template("index.html")

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('secrets'))

    if request.method == "POST":
        data = request.form

        if User.query.filter_by(email=data["email"]).first():
            flash(f"User with email {data['email']} already exists!")
            return redirect(url_for('login'))

        new_user = User(name=data["name"], email=data["email"], password=generate_password_hash(data["password"], method='pbkdf2:sha256', salt_length=8))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)

        return redirect(url_for('secrets'))
    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('secrets'))

    form = LoginForm()
    if request.method == "POST":
        user = db.session.query(User).filter_by(email=form.email.data).first()

        if user == None:
            flash("User doesn't exist!!")
            return redirect(url_for('login'))
        elif check_password_hash(user.password, form.password.data):
            # user = load_user(user.id) this not required
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash('Invalid username or password!')
            return redirect(url_for('login'))

    return render_template("login.html", form=form)

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static','files/cheat_sheet.pdf', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
