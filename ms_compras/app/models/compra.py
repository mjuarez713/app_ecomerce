from dataclasses import dataclass
from datetime import datetime
from app import db



@dataclass(init=False, repr=True ,eq=True)
class Compra(db.Model):
    __tablename__ = 'sells'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto_id: int = db.Column("producto_id", db.Integer, nullable=False)
    fecha_compra: datetime = db.Column(db.DateTime, default=datetime.utcnow, nullable=False) 
    dirección_envio: str = db.Column(db.String(120), nullable=False)

    def __init__(self, producto_id: int = None, direccion_envio: str = None, medio_de_pago: str = None):
        self.producto_id = producto_id
        self.dirección_envio = direccion_envio
        self.medio_de_pago = medio_de_pago

