
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Admin(db.Model):
    '''This represent our admin table in db'''
    id: int = db.Column(db.Integer, primary_key=True)
    first_name: str = db.Column(db.String, nullable=False)
    last_name: str = db.Column(db.String, nullable=False)
    username: str = db.Column(db.String, nullable=False, unique=True)
    email: str = db.Column(db.String, nullable=False, unique=True)
    password: str = db.Column(db.String, nullable=True, unique=False)
    date_joined: datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified: datetime = db.Column(db.DateTime, nullable=True)
    image_file: str = db.Column(db.String, nullable=True, default='avatar.jpg')
    jwt_auth_active = db.Column(db.Boolean())
    is_admin = db.Column(db.Boolean(), default=True)

    def __init__(self):
        pass

    def __repr__(self):
        return f"Admin {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()

    

class Customer(db.Model):
    '''This represent our user table in db'''
    id: int = db.Column(db.Integer, primary_key=True)
    # add user login including google|facebook oauth inclusive.
    

class Product(db.Model):
    '''This represents our addproduct table in db'''

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    description: str = db.Column(db.Text)
    price: str = 0
    currency: str = ''
    info: str = ''
    full_description: str = ''
    slug: str   = '' 
    img_main: str   = ''
    img_card: str = ''
    img_1: str = ''
    img_2: str = ''
    img_3: str = ''
    # product cat
    # product brand

    

class Brand(db.Model):
    '''This represents our brand in db'''
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    


class Category(db.Model):
    '''This represents our category table in db'''
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    

class Cart(db.Model):
    '''this represent our cart table in db'''
    id: int = db.Column(db.Integer, primary_key=True)
    

class NewsLetter(db.Model):
    '''This is for newsletter subscription'''
    id: int = db.Column(db.Integer, primary_key=True)
    email: str = db.Column(db.String, nullable=False, unique=False)
    




