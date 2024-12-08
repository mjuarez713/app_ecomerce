from flask import jsonify, Blueprint, request
from app.mapping import ProductSchema
from app.services import ProductService

product = Blueprint('product', __name__)
service = ProductService()
product_schema = ProductSchema()

@product.route('/', methods=['POST'])
def create():
    product = product_schema.load(request.json)
    resp = product_schema.dump(service.save(product))
    return resp, 201

@product.route('/', methods=['GET'])
def all():
    resp = product_schema.dump(service.all(), many=True) 
    return resp, 200

@product.route('/<int:producto_id>', methods=['GET'])
def find(producto_id):
    resp = product_schema.dump(service.find(id))
    return resp, 200

@product.route('/<string:name>', methods=['GET'])
def find_by_name(name):
    resp = product_schema.dump(service.find_by_name(name))
    return resp, 200  