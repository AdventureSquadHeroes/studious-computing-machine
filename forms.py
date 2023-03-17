from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class SearchForm(FlaskForm):
    cuisine = StringField("Cuisine Type")
    ingredients = StringField("Ingredients")
    equipment = StringField("Type of Equipment used")
    submit = SubmitField("Search")