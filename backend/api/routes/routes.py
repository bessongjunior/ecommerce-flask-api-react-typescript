
import logging


# Register all routes endpointts and versions!
from flask_restx import Api, Resource

# configure root logger
logging.basicConfig(level=logging.INFO)
from api import fh

api = Api()

rest_api = api.namespace('api/v1', description='test')

# configure a file handler for ns1 only
rest_api.logger.addHandler(fh)

@rest_api.route('/my-resource')
class MyResource(Resource):
    def get(self):
        # will log
        rest_api.logger.info("hello from ns1")
        return {"message": "hello"}
