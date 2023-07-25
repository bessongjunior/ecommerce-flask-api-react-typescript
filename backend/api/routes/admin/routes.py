

import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

from flask import request, send_file, send_from_directory, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields, reqparse
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from ...models.models import db, Admin
from ...config import BASE_DIR


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

admin_edit_model = admin_ns.model('EditModel', {
    "username": fields.String(),
    "email": fields.String()
})


parser = reqparse.RequestParser()
upload_parser = admin_ns.parser()
upload_parser.add_argument('profile_picture', 
                           location='files', 
                           type = FileStorage, 
                           required=True, 
                        #    action='append'
                        )

allowed_extensions = set(['jpg', 'png', 'jpeg', 'gif'])

"""Helper function for JWT token required"""

def allowed_file(filename):
    '''check if the file name has our valide extension'''
    for filetype in allowed_extensions:
        return filetype
    # return filetype in allowed_extensions


''' Routes '''


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


@admin_ns.route('/v1/<int:admin_id>/logout')
class LogoutAdmin(Resource):
    ''' Logout resource route'''

    def post(self, admin_id):
        '''Admin Logout endpoint'''

        # _JWT_token = request.headers.get('Authorization')
        # _jwt_token = request.headers["authorization"]

        admin_check = Admin.find_by_id(admin_id)
        print(admin_check)
        admin_check.set_jwt_auth_active(False)
        admin_check.save()

        return {"success": True, "msg": "successfully logged out!"}, HTTPStatus.OK


@admin_ns.route('/v1/<int:admin_id>/edit')
class EditAdminDetails(Resource):
    ''' Logout resource route'''

    @admin_ns.expect(admin_edit_model)
    def patch(self, admin_id):
        '''Admin Logout endpoint'''

        req_data = request.get_json()

        _new_username = req_data.get("username")
        _new_email = req_data.get("email")

        admin_updates = Admin.query.filter_by(id=int(admin_id)).first()
        admin_updates.usename = _new_username
        admin_updates.email = _new_email

        db.session.commit()

        return {"success": True, "msg": "username and email successfully updated."}, HTTPStatus.ACCEPTED

    @admin_ns.expect(upload_parser)
    def put(self, admin_id):
        '''Admin profile picture upload endpoint'''

        args = upload_parser.parse_args()
        file = args['profile_picture']

        admin_updates = Admin.query.filter_by(id=int(admin_id)).first()

        if file is None:
                # add logs
                return {"success": False, "msg": "Field not found, please resend!"}, HTTPStatus.NO_CONTENT
        
        if admin_updates is None:
                # add logs
                return{"success": False, "msg":"The param 'id' mismatch"}, HTTPStatus.BAD_REQUEST
        
        
        if not allowed_file(file.filename):
                # add logs 
                return {'success': False, 'msg': 'file type not accepted'}, HTTPStatus.FORBIDDEN
        
        if allowed_file(file.filename):
                filename = secure_filename(file.filename)
                # print(filename)
                file.save(os.path.join(current_app.config['UPLOAD_PICTURE'], filename))


        filename = secure_filename(file.filename)
        admin_updates.profile = filename

        db.session.commit()

        return {
             "success": True,
             "msg": "Profile picture successfully uploads"
        }, HTTPStatus.ACCEPTED   


    def get(self, admin_id):
        '''Get current admin profile'''

        filename = Admin.query.filter_by(id=admin_id).first()
        directory = os.path.join(current_app.config['UPLOAD_PICTURE'])
        # return send_file(filename.profile, mimetype='image/jpeg')
        # return send_from_directory(directory, filename.profile, as_attachment=False), HTTPStatus.OK
        image_url = url_for('static', filename=f'profile/{filename.profile}', _external=True)
        return {'image_url': image_url}, HTTPStatus.OK




# @admin_ns.route('v1/<admin_id>/profile_picture')
# class UpdateAdminProfilePhoto(Resource):
#     ''' Logout resource route'''

    



