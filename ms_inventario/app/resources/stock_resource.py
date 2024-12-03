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
    if stock.entrada_salida == 1:
      resp = stock_schema.dump(service.ingreso(stock))
    elif stock.entrada_salida == -1:
       resp = stock_schema.dump(service.egreso(stock))
    else:
        return {"error": "entrada_salida debe ser 1 (ingreso) o -1 (egreso)"}, 400
    return resp, 201

@stock.route('/', methods=['GET'])
def all():
    resp = stock_schema.dump(service.all(), many=True) 
    return resp, 200

@stock.route('/stock_total/<int:producto_id>', methods=['GET'])
def stock_total(producto_id):
    try:
        total_stock = service.calcular_stock(producto_id)
        return jsonify({"producto_id": producto_id, "stock_total": total_stock}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
