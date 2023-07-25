

import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = BASE_DIR+'/static/uploads'
UPLOAD_PICTURE = BASE_DIR+'/static/profile'

class BaseConfig():
    '''Carries our basic configuration of the platform'''

    TESTING = False
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///' + os.path.join(BASE_DIR, 'apidata.db')
    # SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@host:port/databse_name' #For production environment ~ replace postgresql with mysql if u want 
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SECRET_KEY = os.environ.get('SECRET_KEY') #os.urandom(24)
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    SECURITY_PASSWORD_SALT= os.environ.get('SECURITY_PASSWORD_SALT')
    SWAGGER_VALIDATOR_URL = 'http://localhost:5000/doc'#'http://domain.com/validator'

    MAIL_PORT: int = 587
    MAIL_USE_TLS: bool = False
    MAIL_USE_SSL: bool = True
    MAIL_SERVER: str = 'smtp.googlemail.com'
    MAIL_DEFAULT_SENDER = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    UPLOAD_FOLDER = UPLOAD_FOLDER
    UPLOAD_PICTURE = UPLOAD_PICTURE
    USE_X_SENDFILE = True
    MAX_CONTENT_LENGTH = 6 * 1000 * 1000




class ProductionConfig(BaseConfig):
    # SQLALCHEMY_DATABASE_URI = <Production DB URL>
    PRODUCTION = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'apidataprod.db')

    