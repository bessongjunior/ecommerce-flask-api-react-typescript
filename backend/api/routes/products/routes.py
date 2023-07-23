




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







allowed_extensions = set(['image/jpeg', 'image/png', 'jpeg', 'gif'])

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


