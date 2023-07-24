

import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

from flask import request, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename

from ...models.models import db, Admin


admin_ns = Namespace('admin', description='Admin related operations')


# configure a file handler for admin namespace only
admin_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
admin_ns.logger.addHandler(fh)

admin_reg_model = admin_ns.model('RegistrationModel', {
    "firstname": fields.String(),
    "lastname": fields.String(),
    "username": fields.String(),
    "email": fields.String(), 
    "password": fields.String(),
})

admin_login_model = admin_ns.model('LoginModel', {
    "email": fields.String(),
    "password": fields.String()
})

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
    


@admin_ns.route('/v1/register')
class RegisterAdmin(Resource):
    ''' Registration resource route'''

    @admin_ns.expect(admin_reg_model)
    async def post(self, **kwargs):
        '''Admin registration endpoint'''

        req_data = await request.get_json()

        _firstname = req_data.get('firstname')
        _lastname = req_data.get('lastname')
        _username = req_data.get('username')
        _email = req_data.get('email')
        _password = req_data.get('password')

        # return {'req_data' : req_data}, HTTPStatus.OK

        # check if user email exist
        check_email = Admin.find_by_email(_email)
        
        if not check_email is None:
            # add logs
            return {
                "Success": False,
                "msg": "email already exits"
            }, HTTPStatus.BAD_REQUEST
        
        new_admin = Admin(first_name=_firstname, last_name=_lastname, username=_username, email=_email)

        new_admin.set_password(_password)

        new_admin.save()

        return {"success": True,
                "userID": new_admin.id,
                "msg": "The user was successfully registered"
                }, HTTPStatus.CREATED

        # check_admin = 

         


@admin_ns.route('/v1/login')
class LoginAdmin(Resource):
    ''' Login resource route'''

    @admin_ns.expect(admin_login_model)
    def post(self):
        '''Admin Login endpoint'''

        req_data = request.get_json()

        _email = req_data.get("email")
        _password = req_data.get("password")

        admin_exists = Admin.find_by_email(_email)

        print(admin_exists)

        if not admin_exists:
            admin_ns.logger.info(f"Administrator donot exist, the email '{_email}' was use, attempting to login on an admin account")
            return {"success": False,
                    "msg": "This email does not exist."}, HTTPStatus.NOT_FOUND

        if not admin_exists.check_password(_password):
            admin_ns.logger.info(f"Administrator exist, the admin with email '{_email}' was use, password did not match")
            return {"success": False,
                    "msg": "Wrong credentials."}, HTTPStatus.NOT_FOUND

        # # create access token uwing JWT
        # # token = jwt.encode({'email': _email, 'exp': datetime.utcnow() + timedelta(minutes=30)}, BaseConfig.SECRET_KEY)

        admin_exists.set_jwt_auth_active(True)
        admin_exists.save()

        return {"success": True,
                # "token": token,
                "user": admin_exists.toJSON()
                }, HTTPStatus.OK


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



