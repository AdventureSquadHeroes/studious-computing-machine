from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from forms import SearchForm, EmailForm
from api import RecipeSearch
from contact import Contact

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/", methods=["POST", "GET"])
def home():
    search_form = SearchForm()
    results = None
    if search_form.validate_on_submit():
        query = RecipeSearch(search_form.cuisine.data,
                             search_form.diet.data,
                             search_form.equipment.data,
                             search_form.ingredients.data,
                             search_form.excluded_ingredients.data, 
                             )
        request = query.search()
        results = [items for items in request['results']]
    return render_template('index.html', form=search_form, results=results)


@app.route('/view/<int:id>', methods=["POST", "GET"])
def view_recipe(id):
    request = RecipeSearch.recipe_search(id)
    return render_template("view.html", recipe=request)


@app.route("/email", methods=["POST", "GET"])
def send_message():
    email_form = EmailForm()
    if email_form.validate_on_submit():
        new_message = Contact(email_form.name.data, 
                              email_form.email.data, 
                              email_form.subject.data, 
                              email_form.body.data
                              )
        Contact.send_message(new_message)
        flash("Message Sent")
        return redirect(url_for("send_message"))
    return render_template("email.html", form=email_form)


if __name__ == '__main__':
    app.run(debug=True)