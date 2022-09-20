from flask import render_template, flash, request, redirect, url_for
from src import app
from admin.forms import RegistrationForm

@app.route("/")
def home():
    return "Homepage of your carts"


@app.route('/register', method=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        flash('Thanks for registering')
        return redirect(url_for('login'))




    return render_template('admin/register.html', title="Register page")
