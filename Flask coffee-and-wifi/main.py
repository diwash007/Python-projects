from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'lol'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    loc = StringField('Google Map URL', validators=[DataRequired(), URL()])
    open_time = StringField('Open time', validators=[DataRequired()])
    close_time = StringField('Close time', validators=[DataRequired()])
    coffee = SelectField('Coffee rating', validators=[DataRequired()], choices=[0,1,2,3,4,5])
    wifi = SelectField('Wifi rating', validators=[DataRequired()], choices=[0,1,2,3,4,5])
    power = SelectField('Power rating', validators=[DataRequired()], choices=[0,1,2,3,4,5])
    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST','GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a') as f:
            f.write(f"\n{form.cafe.data},{form.loc.data},{form.open_time.data},{form.close_time.data},{form.coffee.data},{form.wifi.data},{form.power.data}")
        return redirect('/cafes')
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
