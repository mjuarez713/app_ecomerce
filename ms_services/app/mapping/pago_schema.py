from marshmallow import validate, fields, Schema, post_load
from app.models import Payment

class PaymentSchema(Schema):
    id = fields.Integer(required=False)
    producto_id = fields.Integer(required=False)
    precio = fields.Float(required=False)
    medio_de_pago = fields.String(required=False)
    #deleted_at = fields.DateTime(required=False, allow_none=True)

    @post_load
    def make_pago(self, data, **kwargs):
        pago = Payment()
        for key, value in data.items():
            setattr(pago, key, value)
        return pago