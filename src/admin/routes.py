from flask import render_template, flash, request, redirect, url_for
from src import app
from admin.forms import RegistrationForm
from model import User


@app.route("/")
def home():
    return "Homepage of your carts"


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('login'))

    return render_template('admin/register.html', form=form)
