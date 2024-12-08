from app.models import Compra
from marshmallow import fields, Schema, post_load, EXCLUDE

class CompraSchema(Schema):
    class Meta:
        unknown = EXCLUDE 
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    fecha_compra = fields.DateTime(required=False)
    cantidad = fields.Integer(required=True)
    direccion_envio = fields.String(required=True) 

    @post_load
    def make_stock(self, data, **kwargs):
        return Compra(**data)
