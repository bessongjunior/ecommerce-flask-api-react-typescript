

import logging
from http import HTTPStatus

from flask_restx import Namespace, Resource, fields
from flask import request

from ...models.models import db, Brand

brand_ns = Namespace('brand', description='Branding operations')

brand_ns.logger.setLevel(logging.INFO)
fh = logging.FileHandler("v1.log")
brand_ns.logger.addHandler(fh)


'''Defining model / schema validation'''

addbrand_model = brand_ns.model('Addbrand', {'name': fields.String()})

brand_model = brand_ns.model('AllBrands', {"id":fields.Integer(), "name": fields.String()})

# update_brand = brand_ns.model('Updatebrand', {'name': })


'''Routes'''

@brand_ns.route('/v1/brands')
class GetAllBrands(Resource):
    '''This resource if for the get all brand endpoint'''

    @brand_ns.marshal_with(brand_model, envelope='data')
    async def get(self, **kwargs):
        '''Endpoint retuns all our brand'''

        # same output as using the @brand_ns.marshal_with api
        # values = Brand.query.all()

        # result = {
        #   'data':  [ {'id': value.id, 'name': value.name} for value in values]
        # }

        return Brand.query.all(), HTTPStatus.OK
        # return result, HTTPStatus.OK



@brand_ns.route('/v1/addbrand/')
class AddBrand(Resource):
    '''This resource creates the add brand endpoint'''

    @brand_ns.expect(addbrand_model)
    async def post(self):
        '''This is the add brand endpoint'''

        req_data = request.get_json()

        _name = req_data.get('name')

        # check if name exist
        brand_exist = Brand.get_by_name(_name)

        if brand_exist:
            # add logs
            return {"success" : False, 
                    "msg": "The name entered already exist"
                    }, HTTPStatus.BAD_REQUEST
        
        new_cat = Brand(name=_name)

        new_cat.save()

        return {"success": True,
                "msg": "Category added with success"
                }, HTTPStatus.CREATED
    

@brand_ns.route('/v1/<int:brand_id>/brand')
class BrandUpdateDelete(Resource):
    '''This resource is design to update and delete a brand endpoints'''

    async def patch(self, brand_id):
        '''Endpoint to update a brand in db'''

        req_data = request.get_json()
        _new_name = req_data.get('name')

        brand_exists = Brand.get_by_id(brand_id)

        if brand_exists is None:
            # add logs
            return{ "success" : False,
                    "msg" : "The brand doesn't exist" 
                    }, HTTPStatus.NOT_FOUND
        
        brand_exists.name = _new_name
        db.session.commit()

        return {"success" : True,
                "msg" : "Brand successfully updated"
            }, HTTPStatus.ACCEPTED


    async def delete(self, brand_id):
        '''Endpoint to delete brand in db'''

        brand_exists = Brand.get_by_id(brand_id)

        if not brand_exists:
            # add logs
            return{ "success" : False,
                    "msg" : "The brand doesn't exist" 
                    }, HTTPStatus.NOT_FOUND
        
        db.session.delete(brand_exists)
        db.session.commit()
        return {"success" : True,
                "msg" : "Brand successfully deleted"
            }, HTTPStatus.OK