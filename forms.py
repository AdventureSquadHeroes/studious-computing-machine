from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    cuisine = StringField("Search by cuisine type")
    ingredients = StringField("Search by ingredients")
    equipment = StringField("Search by type of equipment used")
    submit = SubmitField("Search")


class EmailForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject")
    body = StringField("Message", validators=[DataRequired()], render_kw={"style": "height: 250px"})
    submit = SubmitField("Send")