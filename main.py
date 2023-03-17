from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from forms import SearchForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

@app.route("/")
def home():
    search_form = SearchForm()
    return render_template('index.html', form=search_form)



if __name__ == '__main__':
    app.run(debug=True)