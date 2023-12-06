from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import Loginform
@app.route('/')
@app.route('/home')
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/about_me')
def about_me():
    """About Me URL"""
    return render_template('about_me.html', title='About Me Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = Loginform()
    if form.validate_on_submit():
        flash(f'You are requesting to login {form.username.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login', form=form)

