
from flask import Flask, render_template
from data.db import get_Pizzas
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas_db = get_Pizzas()
    pizzas = []
    for pizza in pizzas_db:
        pizzas.append(
            {"name": pizza[1], "ingredients": pizza[2], "price": pizza[3]}
        )

    context = {
        "pizzas": pizzas,
        "title": "Мега меню"
    }
    return render_template("menu.html", **context)


if __name__ == '__main__':
    app.run(debug=True)












