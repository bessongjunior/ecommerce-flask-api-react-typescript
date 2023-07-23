

import json
import time
import logging
# from logging.config import dictConfig
from logging.handlers import SMTPHandler

from flask import Flask, Response
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from celery import Celery
from werkzeug.middleware.proxy_fix import ProxyFix



# app modules import
from .models.models import db
from .utils.mail import mail
from .routes.routes import rest_api

# dictConfig({
#     'version': 1,
#     'formatters': {'default': {
#         'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
#     }},
#     'handlers': {'wsgi': {
#         'class': 'logging.StreamHandler',
#         'stream': 'ext://flask.logging.wsgi_errors_stream',
#         'formatter': 'default'
#     }},
#     'root': {
#         'level': 'INFO',
#         'handlers': ['wsgi']
#     }
# })

app = Flask(__name__)

app.wsgi_app = ProxyFix(app.wsgi_app)

app.config.from_object('api.config.BaseConfig')    

db.init_app(app)

mail.init_app(app)

CORS(app)

JWTManager(app)

migrate = Migrate(app, db)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

def make_celery(app):
    celery = Celery(
        app.import_name, broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

celery = make_celery(app)

mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['admin@example.com'],
    subject='Application Error'
    )
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
'[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))
if not app.debug:
    app.logger.addHandler(mail_handler)

# add routes endpoints here
rest_api.init_app(app)

# db setup
@app.before_request
def initialize_database() -> None:
    '''creates database'''
    db.create_all()


# response setup
@app.after_request
def after_request(response) -> Response:
    '''Sends back a custom error with {"success", "msg"} format'''

    if int(response.status_code) >= 400:
        response_data = json.loads(response.get_data())
        if "errors" in response_data:
            response_data = {"success": False,
                             "msg": list(response_data["errors"].items())[0][1]}
            response.set_data(json.dumps(response_data))
        response.headers.add('Content-Type', 'application/json')
    return response