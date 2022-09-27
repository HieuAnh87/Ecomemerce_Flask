from flask import render_template, request, redirect, session, url_for, Flask, flash
from src import app, db, photos
from .forms import Addproducts
from .models import Brand, Category, Addproduct
import secrets


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
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
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    if request.method == "POST":
        getcategory = request.form.get('category')
        category = Category(name=getcategory)
        db.session.add(category)
        db.session.commit()
        flash(f'The categpry {getcategory} was added to your database!', 'success')
        return redirect(url_for('addcategory'))
    return render_template('products/addbrand.html', category='category')


@app.route('/addproduct', methods=['POST', 'GET'])
def addproduct():
    if 'email' not in session:
        flash('Please login first!', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.all()
    categories = Category.query.all()
    form = Addproducts(request.form)
    if request.method == "POST":
        name = form.name.data
        price = form.price.data
        discount = form.discount.data
        stock = form.stock.data
        colors = form.colors.data
        desc = form.description.data
        brand = request.form.get('brand')
        category = request.form.get('category')
        image_1 = photos.save(request.files.get('image_1'), name=secrets.token_hex(10) + ".")
        image_2 = photos.save(request.files.get('image_2'), name=secrets.token_hex(10) + ".")
        image_3 = photos.save(request.files.get('image_3'), name=secrets.token_hex(10) + ".")
        addproduct = Addproduct(name=name,
                                price=price,
                                discount=discount,
                                stock=stock,
                                colors=colors,
                                desc=desc,
                                category_id=category,
                                brand_id=brand,
                                image_1=image_1,
                                image_2=image_2,
                                image_3=image_3)
        db.session.add(addproduct)
        flash(f'The product {name} was added in database', 'success')
        db.session.commit()

    return render_template('products/addproduct.html', title="Add Product page", form=form, brands=brands,
                           categories=categories)
