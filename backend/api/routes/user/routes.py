



import os
from datetime import datetime, timezone, timedelta

from functools import wraps
from http import HTTPStatus
import logging

from flask import request, url_for, current_app, render_template
from flask_restx import Namespace, Resource, fields
from werkzeug.utils import secure_filename


user_ns = Namespace('user', description='User related operations')


# configure a file handler for admin namespace only
user_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
user_ns.logger.addHandler(fh)







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


