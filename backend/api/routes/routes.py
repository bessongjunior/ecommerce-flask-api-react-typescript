
# import logging


# Register all routes endpointts and versions!
from flask_restx import Api
# from flask import #url_for, current_app, json

# configure root logger
# logging.basicConfig(level=logging.INFO)


from .admin.routes import admin_ns as admin_api
from .customer.routes import user_ns as user_api
from .products.routes import product_ns as product_api
from .brand.routes import brand_ns as brand_api
from .category.routes import category_ns as category_api


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
rest_api.add_namespace(user_api)
rest_api.add_namespace(product_api)
rest_api.add_namespace(brand_api)
rest_api.add_namespace(category_api)

