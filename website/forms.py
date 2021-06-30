from wtforms import Form, StringField, PasswordField, IntegerField, SubmitField, TextAreaField, validators
from flask_wtf.file import FileAllowed,FileField,FileRequired

class RegistrationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.DataRequired()])
    department=StringField('Department')
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(Form): 
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email(),validators.DataRequired()])
    department=StringField('Department')
    password = PasswordField('Password', [validators.DataRequired()])

class AddProducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    discount = IntegerField('Discount')
    quantity = IntegerField('Quantity',[validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    color = TextAreaField('Color',[validators.DataRequired()])
    brand=StringField('Name',[validators.DataRequired()])

    image_1 = FileField('Image ', validators=[FileRequired(), FileAllowed(['jpg','png','gif','jpeg'])])
    
class CustomerRegistrationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    username = StringField('Username', [validators.Length(min=4, max=25),validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email(),validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    country = StringField('Country', [validators.Length(min=4, max=25),validators.DataRequired()])
    city = StringField('City', [validators.Length(min=4, max=25),validators.DataRequired()])
    contact = StringField('Contact', [validators.Length(min=4, max=25),validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=4, max=25),validators.DataRequired()])
    zipcode = StringField('Zipcode', [validators.Length(min=4, max=25),validators.DataRequired()])
    submit=SubmitField('Register')

class CustomerLoginForm(Form): 
    username = StringField('Username', [validators.Length(min=4, max=25),validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])

class OfflineOrderForm(Form):
    first_name = StringField('First Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    last_name = StringField('Last Name', [validators.Length(min=4, max=25),validators.DataRequired()])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email(),validators.DataRequired()])
    order = TextAreaField('Order',[validators.DataRequired()])
    country = StringField('Country', [validators.Length(min=4, max=25),validators.DataRequired()])
    city = StringField('City', [validators.Length(min=4, max=25),validators.DataRequired()])
    contact = StringField('Contact', [validators.Length(min=4, max=25),validators.DataRequired()])
    address = StringField('Address', [validators.Length(min=4, max=25),validators.DataRequired()])
    zipcode = StringField('Zipcode', [validators.Length(min=4, max=25),validators.DataRequired()])
    

    
