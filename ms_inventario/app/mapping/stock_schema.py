from app.models import Stock
from marshmallow import fields, Schema, post_load

class StockSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_transaccion = fields.DateTime(required=True)
    cantidad = fields.Integer(required=True)
    entrada_salida = fields.Integer(required=True)
