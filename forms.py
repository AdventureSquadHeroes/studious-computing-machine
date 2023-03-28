from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from flask_ckeditor import CKEditorField

class SearchForm(FlaskForm):
    cuisine = StringField("Search by Cuisine type")
    diet = StringField("Search by Diet")
    equipment = StringField("Search by Cooking Equipment")
    ingredients = StringField("Search by Ingredients")
    excluded_ingredients = StringField("Exclude by Ingredients")
    submit = SubmitField("Search")


class EmailForm(FlaskForm):

    def is_email(form, email):
        if "@" not in email.data or "." not in email.data:
            raise ValidationError("That is not a valid email address")
    
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), is_email])
    subject = StringField("Subject")
    body = CKEditorField("Message", validators=[DataRequired()], render_kw={"style": "height: 250px"})
    submit = SubmitField("Send")

    