from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError


app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)