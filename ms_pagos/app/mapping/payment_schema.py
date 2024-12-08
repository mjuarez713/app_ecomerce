from app.models import Payment
from marshmallow import fields, Schema, post_load

class PaymentSchema(Schema):
    id = fields.Integer(dump_only=True)
    producto_id = fields.Integer(required=True)
    precio: float = fields.Float(required=True)
    medio_de_pago: str = fields.String(required=True)

    @post_load
    def make_stock(self, data, **kwargs):
        return Payment(**data)
