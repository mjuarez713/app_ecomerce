from flask import jsonify, Blueprint, request
from app.mapping import PaymentSchema
from app.services import PaymentService

payment = Blueprint('payment', __name__)
service = PaymentService()
payment_schema = PaymentSchema()

"""
Crea nueva Tarea
"""
@payment.route('/', methods=['POST'])
def create():
    payment = payment_schema.load(request.json)
    resp = payment_schema.dump(service.save(payment))
    return resp, 201


@payment.route('/', methods=['GET'])
def all():
    resp = payment_schema.dump(service.all(), many=True) 
    return resp, 200


