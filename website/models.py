from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class Customer(db.Model, UserMixin):
       __tablename__='customers'

       id = db.Column(db.Integer, primary_key=True)
       first_name = db.Column(db.String(150),index=True,nullable=False)
       last_name = db.Column(db.String(150),index=True,nullable=False)
       username = db.Column(db.String(150),index=True,unique=True,nullable=False)
       email = db.Column(db.String(150),unique=True,nullable=False)
       password= db.Column(db.String(150),unique=False, nullable=False)
       country = db.Column(db.String(50),nullable=False)
       city = db.Column(db.String(50),nullable=False)
       contact = db.Column(db.String(50),unique=True,nullable=False)
       address = db.Column(db.String(50),nullable=False)
       zipcode = db.Column(db.String(50),nullable=False)
       date_registered =db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
       
       def __repr__(self):
          return '<Customer: {}>'.format(self.name)


class Employee(db.Model):
       __tablename__='employees'

       id = db.Column(db.Integer, primary_key=True)
       first_name = db.Column(db.String(150),index=True)
       last_name = db.Column(db.String(150),index=True)
       email = db.Column(db.String(150),index=True,unique=True)
       password = db.Column(db.String(150)) 
       department_id = db.Column(db.String(150), db.ForeignKey('departments.id'))

       department = db.relationship('Department',backref=db.backref('departments', lazy=True))

       def __repr__(self):
          return '<Employee: {}>'.format(self.name)


class Department(db.Model):
       __tablename__='departments'

       id = db.Column(db.Integer, primary_key=True)
       dept= db.Column(db.String(60), unique=True)
       #employees = db.relationship('Employee', backref='department',lazy='dynamic')

       def __repr__(self):
          return '<Department: {}>'.format(self.name)

class AddProduct(db.Model):
       __tablename__='products'

       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(150),unique=True,nullable=False)
       price = db.Column(db.Integer, nullable=False)
       discount = db.Column(db.Integer)
       color=db.Column(db.Text,nullable=False)
       description = db.Column(db.String(300),nullable=False)
       quantity = db.Column(db.Integer)
       image_1=db.Column(db.String(150),nullable=False,default='img1.jpg')
       brand_id= db.Column(db.Integer,db.ForeignKey('brands.id'),nullable=False)
       category_id= db.Column(db.Integer,db.ForeignKey('categories.id'),nullable=False)
       
       brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))
       category = db.relationship('Category',backref=db.backref('categories', lazy=True))

       def __repr__(self):
          return '<AddProduct: {}>'.format(self.name)


class Brand(db.Model):
       __tablename__='brands'

       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(150),unique=True,nullable=False)

class Category(db.Model):
       __tablename__='categories'

       id = db.Column(db.Integer, primary_key=True)
       name = db.Column(db.String(150),unique=True,nullable=False)

class Shipper(db.Model):
       __tablename__='shippers'

       id = db.Column(db.Integer, primary_key=True)
       email = db.Column(db.String(150),unique=True)
       company_name = db.Column(db.String(150))
       contact = db.Column(db.String(150))
       

class Order(db.Model):
       __tablename__='orders'

       id = db.Column(db.Integer, primary_key=True)
       customer= db.Column(db.Integer,db.ForeignKey('customers.id'),nullable=False)
       price = db.Column(db.Integer, unique=True)
       quantity = db.Column(db.Integer)
       date=db.Column(db.DateTime(timezone=True),default=func.now())
       

class Orderdetail(db.Model):
       __tablename__='orderdetails'

       id = db.Column(db.Integer, primary_key=True)
       total_price = db.Column(db.Integer, unique=True)
       quantity = db.Column(db.Integer)



