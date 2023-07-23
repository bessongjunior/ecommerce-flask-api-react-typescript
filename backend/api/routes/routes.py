
import logging


# Register all routes endpointts and versions!
from flask_restx import Api, Resource

# configure root logger
logging.basicConfig(level=logging.INFO)


from .admin.routes import admin_ns as admin_api



# configure a file handler for ns1 only
# rest_api.logger.addHandler(fh)

# @rest_api.route('/my-resource')
# class MyResource(Resource):
#     def get(self):
#         # will log
#         rest_api.logger.info("hello from ns1")
#         return {"message": "hello"}



rest_api = Api(title="Ecommerce Platform API", version="1.0", description=" This is a dedicated backend for a flask/react web app.")

rest_api.add_namespace(admin_api)


