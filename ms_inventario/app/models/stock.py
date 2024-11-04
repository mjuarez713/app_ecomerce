from dataclasses import dataclass
from datetime import datetime
from app import db

@dataclass
class Stock(db.Model):
    __tablename__ = 'stock'

    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column(db.Integer, nullable=False) 
    fecha_transaccion: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    cantidad: float = db.Column(db.Float, nullable=False) 
    entrada_salida: int = db.Column(db.Integer, nullable=False, default=1) #maneja 1 y 2 
    #en schema tiene que haber un validador de 1 o 2

    def __init__(self, producto_id: int = None, cantidad: int = None, entrada_salida: int = None):
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.entrada_salida = entrada_salida
        self.fecha_transaccion = datetime.utcnow() 
