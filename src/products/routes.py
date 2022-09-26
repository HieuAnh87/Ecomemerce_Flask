from flask import render_template, request, redirect, session, url_for, Flask, flash
from src import app, db
from .models import Brand, Category


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        db.session.commit()
        flash(f'The brand {getbrand} was added to your database!', 'success')
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', brands='brands')


@app.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    if request.method == "POST":
        getcategory = request.form.get('category')
        category = Brand(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'The categpry {getcategory} was added to your database!', 'success')
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html', category='category')
