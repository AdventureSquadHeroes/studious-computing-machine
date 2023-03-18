from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import SearchForm
from api import RecipeSearch

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/", methods=["POST", "GET"])
def home():
    search_form = SearchForm()
    results = None
    if search_form.validate_on_submit():
        query = RecipeSearch(search_form.ingredients.data, search_form.cuisine.data, search_form.equipment.data)
        request = query.search()
        results = [items for items in request['results']]
    return render_template('index.html', form=search_form, results=results)


@app.route('/view/<int:id>', methods=["POST", "GET"])
def view_recipe(id):
    request = RecipeSearch.recipe_search(id)
    print(request)
    return render_template("view.html", recipe=request)


if __name__ == '__main__':
    app.run(debug=True)