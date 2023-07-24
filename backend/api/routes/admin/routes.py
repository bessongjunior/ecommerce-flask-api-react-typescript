

import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

from flask import request, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename


admin_ns = Namespace('admin', description='Admin related operations')


# configure a file handler for admin namespace only
admin_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
admin_ns.logger.addHandler(fh)


allowed_extensions = set(['jpg', 'png', 'jpeg', 'gif'])

"""Helper function for JWT token required"""

def allowed_file(filename):
    '''check if the file name has our valide extension'''
    for filetype in allowed_extensions:
        return filetype
    # return filetype in allowed_extensions


''' Routes '''


@admin_ns.route('/test')
class SampleTest(Resource):
    '''Sample test resource routing'''

    async def get(self):
        admin_ns.logger.info("hello from tdd case setup")
        return {"key":"value"}, 200
    


@admin_ns.route('v1/register')
class RegisterAdmin(Resource):
    ''' Registration resource route'''

    async def post(self):
        '''Admin registration endpoint'''

        pass


@admin_ns.route('v1/login')
class LoginAdmin(Resource):
    ''' Login resource route'''

    async def post(self):
        '''Admin Login endpoint'''

        pass


@admin_ns.route('v1/logout')
class LogoutAdmin(Resource):
    ''' Logout resource route'''

    def post(self):
        '''Admin Logout endpoint'''

        pass


@admin_ns.route('v1/<admin_id>/edit')
class EditAdminDetails(Resource):
    ''' Logout resource route'''

    def patch(self, admin_id):
        '''Admin Logout endpoint'''

        pass


@admin_ns.route('v1/<admin_id>/profile_picture')
class UpdateAdminProfilePhoto(Resource):
    ''' Logout resource route'''

    def put(self, admin_id):
        '''Admin Logout endpoint'''

        pass



