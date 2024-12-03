from flask import jsonify, Blueprint, request
from app.mapping import CompraSchema
from app.services import CompraService

compra = Blueprint('sell', __name__)
service = CompraService()
compra_schema = CompraSchema()

@compra.route('/', methods=['POST'])
def create():
    compra = compra_schema.load(request.json)
    resp = compra_schema.dump(service.save(compra))
    return resp, 201