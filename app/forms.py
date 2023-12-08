from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length


class Loginform(FlaskForm):
    """Login Form"""
    username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
    email = StringField('Email Addess', validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class Productform(FlaskForm):
    """Add Product Form"""
    product_name = StringField('Product Name', validators=[DataRequired(), Length(1, 64)])
    product_description = TextAreaField('Product Description', validators=[DataRequired()])
    stock_available = SelectField('Stock Available', validators=[DataRequired()], 
                                  choices=[('1', '1'), ('4', '4'), ('8', '8')])
    submit = SubmitField('Submit')
