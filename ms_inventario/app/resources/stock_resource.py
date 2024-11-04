from flask import jsonify, Blueprint, request
from app.mapping import StockSchema
from app.service import StockService

stock = Blueprint('stock', __name__)
service = StockService()
stock_schema = StockSchema()

"""
Crea nueva Tarea
"""
@stock.route('/', methods=['POST'])
def create():
    stock = stock_schema.load(request.json)
    resp = stock_schema.dump(service.ingreso(stock))
    return resp, 201

@stock.route('/', methods=['GET'])
def all():
    resp = stock_schema.dump(service.all(), many=True) 
    return resp, 200