from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import Loginform, Productform
@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add Product URL"""
    form = Productform()
    if form.validate_on_submit():
        flash(f'You are requesting to add a product {form.product_name.data}')
        return redirect(url_for('index'))
    return render_template('add_product.html', title='Add Product', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = Loginform()
    if form.validate_on_submit():
        flash(f'You are requesting to register {form.username.data}')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

