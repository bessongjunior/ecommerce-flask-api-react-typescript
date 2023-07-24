
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
    # image_file: str = db.Column(db.String, nullable=True, default='avatar.jpg')
    profile = db.Column(db.String, unique=False, nullable=False, default='profile.jpg')
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
    firstname = db.Column(db.String(50), unique= False)
    lastname = db.Column(db.String(50), unique= False)
    username = db.Column(db.String(50), unique= True)
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(200), unique= False)
    country = db.Column(db.String(50), unique= False)
    # state = db.Column(db.String(50), unique= False)
    city = db.Column(db.String(50), unique= False)
    contact = db.Column(db.String(50), unique= False)
    address = db.Column(db.String(50), unique= False)
    zipcode = db.Column(db.String(50), unique= False)
    profile = db.Column(db.String(200), unique= False , default='profile.jpg')
    date_joined = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    date_modified: datetime = db.Column(db.DateTime, nullable=True)
    # add user login including google|facebook oauth inclusive.

    def __init__(self):
        pass

    def __repr__(self):
        return f"Admin {self.username}"

    def save(self):
        db.session.add(self)
        db.session.commit()
    


class CustomerOrder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    invoice = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)
    customer_id = db.Column(db.Integer, unique=False, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    # orders = db.Column(db.Text)


class Product(db.Model):
    '''This represents our addproduct table in db'''

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False, unique=True)
    description: str = db.Column(db.Text)
    price: str = db.Column(db.Numeric(10,2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    info: str = db.Column(db.Text, nullable=True)
    full_description: str = db.Column(db.Text, nullable=True)
    img_main: str   = db.Column(db.String(150), nullable=False, default='main.jpg')
    # slug: str   = 
    # currency: str = 

    def __init__(self):
        pass

    def __repr__(self):
        return f"Product {self.name}"

    def save(self):
        db.session.add(self)
        db.session.commit()
    

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('categories', lazy=True))

    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'),nullable=False)
    brand = db.relationship('Brand',backref=db.backref('brands', lazy=True))

    img_1: str = db.Column(db.String(150), nullable=False, default='image1.jpg')
    img_2: str = db.Column(db.String(150), nullable=False, default='image2.jpg')
    img_3: str = db.Column(db.String(150), nullable=False, default='image3.jpg')
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
    




