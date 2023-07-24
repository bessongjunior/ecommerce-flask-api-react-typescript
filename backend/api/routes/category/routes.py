

import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource, fields
from flask import request

from ...models.models import db, Category

category_ns = Namespace('category', description='Category operations')

category_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
category_ns.logger.addHandler(fh)



'''Defining model / schema validation'''

addcategory_model = category_ns.model('AddCategory', {'name': fields.String()})

category_model = category_ns.model('AllCategories', {"id":fields.Integer(), "name": fields.String()})

'''Routes'''

@category_ns.route('/v1/categories')
class GetAllCategories(Resource):
    '''This resource if for the get all brand endpoint'''

    @category_ns.marshal_with(category_model, envelope='data')
    async def get(self, **kwargs):
        '''Endpoint retuns all our brand'''

        return Category.query.all(), HTTPStatus.OK



# @category_ns.route('/v1/addcategory')
@category_ns.route('/v1/addcategory')
class AddCategory(Resource):
    '''This resource creates the add category endpoint'''
    
    @category_ns.expect(addcategory_model)
    async def post(self):
        '''This is the add category endpoint'''
        

        req_data = request.get_json()

        _name = req_data.get('name')
        
        # check if cat exist
        category_exist = await Category.get_by_name(_name)
        
        if category_exist:
            # add logs
            return {"success" : False, 
                    "msg": "The name entered already exist"
                    }, HTTPStatus.BAD_REQUEST
        
        new_cat = Category(name =_name)

        new_cat.save()

        return {"success": True,
                "msg": "Category added with success"
                }, HTTPStatus.CREATED
    


@category_ns.route('/v1/<int:category_id>/category')
class CategoryUpdateDelete(Resource):
    '''This resource is design to update and delete a category endpoints'''


    async def patch(self, category_id):
        '''Endpoint to update a category in db'''

        req_data = request.get_json()
        _new_name = req_data.get('name')

        category_exists = Category.get_by_id(category_id)

        if category_exists is None:
            # add logs
            return{ "success" : False,
                    "msg" : "The category doesn't exist" 
                    }, HTTPStatus.NOT_FOUND
        
        category_exists.name = _new_name
        db.session.commit()

        return {"success" : True,
                "msg" : "Category successfully updated"
            }, HTTPStatus.ACCEPTED


    async def delete(self, category_id):
        '''Endpoint to delete category in db'''

        # req_data = request.get_json()

        category_exists = await Category.get_by_id(category_id)
        print(category_exists)

        if not category_exists:
            # add logs
            return{ "success" : False,
                    "msg" : "The Category doesn't exist" 
                    }, HTTPStatus.NOT_FOUND
        

        db.session.delete(category_exists)
        db.session.commit()
        return {"success" : True,
                "msg" : "Category successfully deleted"
            }, HTTPStatus.OK

        