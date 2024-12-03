from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Payment(db.Model):
    __tablename__ = 'payment'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column(db.Integer, nullable=False) 
    precio: float = db.Column(db.Float, nullable=False)
    medio_de_pago: str =db.Column(db.String, nullable=False)

    def __init__(self, producto_id: int = None, precio: float = None, medio_de_pago: str = None):
        self.producto_id = producto_id
        self.precio = precio
        self.medio_de_pago = medio_de_pago
