

from .models import db, Brand, Category, Product, Customer, Admin, Cart


def brands():
    brands = Brand.query.join(Product, (Brand.id == Product.brand_id)).all()
    return brands

def categories():
    categories = Category.query.join(Product,(Category.id == Product.category_id)).all()
    return categories