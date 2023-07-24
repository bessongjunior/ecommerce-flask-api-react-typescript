



import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

# from flask import request, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename




user_ns = Namespace('user', description='User related operations')


# configure a file handler for admin namespace only
user_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
user_ns.logger.addHandler(fh)


#   def index():
#         response = make_response(render_template('index.html', foo=42))
#         response.headers['X-Parachutes'] = 'parachutes are cool'
#         return response
# This function accepts the very same arguments you can return from a view function. This for example creates a response with a 404 error code:

#     response = make_response(render_template('not_found.html'), 404)
# The other 




allowed_extensions = set(['png', 'jpg' 'jpeg', 'gif'])

"""Helper function for JWT token required"""

def allowed_file(filename):
    '''check if the file name has our valide extension'''
    for filetype in allowed_extensions:
        return filetype
    # return filetype in allowed_extensions


''' Routes '''


@user_ns.route('/test')
class SampleTest(Resource):
    '''Sample test resource routing'''

    # @user_ns.doc()
    def get(self):
        user_ns.logger.info("hello from tdd case setup user")
        return {"message":"hello"}, 200


@user_ns.route('v1/register')
class RegisterCustomer(Resource):
    ''' Registration resource route'''

    def post(self):
        '''Customer registration endpoint'''

        pass


@user_ns.route('v1/login')
class LoginCustomer(Resource):
    ''' Login resource route'''

    def post(self):
        '''Customer Login endpoint'''

        pass


@user_ns.route('v1/logout')
class LogoutCustomer(Resource):
    ''' Logout resource route'''

    def post(self):
        '''Customer Logout endpoint'''

        pass


@user_ns.route('v1/<customer_id>/edit')
class EditCustomerDetails(Resource):
    ''' Logout resource route'''

    def patch(self, customer_id):
        '''Customer Logout endpoint'''

        pass


@user_ns.route('v1/<customer_id>/profile_picture')
class UpdateCustomerProfilePhoto(Resource):
    ''' Logout resource route'''

    def put(self, customer_id):
        '''Customer Logout endpoint'''

        pass


@user_ns.route('v1/<customer_id>/Invoice')
class CustomerInvoice(Resource):
    ''' Invoice resource route'''

    def post(self, customer_id):
        '''Customer Invoice endpoint'''

        pass


@user_ns.route('v1/<customer_id>/order')
class CustomerOrder(Resource):
    ''' Order resource route'''

    def post(self, customer_id):
        '''Customer Order endpoint'''

        pass