from flask import render_template

from src import app


@app.route("/")
def home():
    return "Homepage of your carts"


@app.route('/register')
def register():
    return render_template('admin/register.html', title="Register user")
