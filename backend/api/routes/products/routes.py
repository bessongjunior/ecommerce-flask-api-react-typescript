




import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

from flask import request, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename


product_ns = Namespace('product', description='Product operations')


# configure a file handler for admin namespace only
product_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
product_ns.logger.addHandler(fh)







allowed_extensions = set(['jpg', 'png', 'jpeg', 'gif'])

"""Helper function for JWT token required"""

def allowed_file(filename):
    '''check if the file name has our valide extension'''
    for filetype in allowed_extensions:
        return filetype
    # return filetype in allowed_extensions


''' Routes '''


@product_ns.route('/test')
class SampleTest(Resource):
    '''Sample test resource routing'''

    async def get(self):
        product_ns.logger.info("hello from tdd case setup product")
        return {"message":"greetings"}, 200

@product_ns.route('/v1/<param>/search_result')
class SearchProduct(Resource):
    '''This resource return search item'''

    def post(self, param):
        '''Search item endpoint'''

        pass

@product_ns.route('/v1/product')
class AllProduct(Resource):
    '''This resource return all products in pagination'''

    def post(self, product_id):
        '''products endpoint'''

        pass

@product_ns.route('/v1/<product_id>/product')
class ProductDetails(Resource):
    '''This resource return search item'''

    def post(self, product_id):
        '''product details endpoint'''

        pass


@product_ns.route('/v1/<brand_id>/seach')
class BrandProduct(Resource):
    '''Get all brands in db'''

    def post(self, brand_id):
        '''Get products by brands'''

        pass

@product_ns.route('/v1/<category_id>/seach')
class BrandProduct(Resource):
    '''Get all brands in db'''

    def post(self, category_id):
        '''Get products by category'''

        pass



# add/update/delete - product, brand , categories!!! goes to admin routes


