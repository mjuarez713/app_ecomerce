from app.models import Product
from marshmallow import fields, Schema, post_load

class ProductSchema(Schema):
    id = fields.Integer(dump_only=True) 
    name = fields.String(required=True) 
    price = fields.Float(required=True)  
    state = fields.Boolean(required=True) 

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data) 