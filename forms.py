from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

class SearchForm(FlaskForm):
    cuisine = StringField("Search by cuisine type")
    ingredients = StringField("Search by ingredients")
    equipment = StringField("Search by type of equipment used")
    submit = SubmitField("Search")