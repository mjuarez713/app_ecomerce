from dataclasses import dataclass
import datetime
from app import db



@dataclass(init=False, repr=True ,eq=True)
class Compra(db.Model):
    __tablename__ = 'compras'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    producto: int = db.Column("producto_id", db.Integer, nullable=False)
    fecha_compra: datetime = db.Column(db.DatetTime, nullable=False)
    dirección_envio: int = db.Column(db.String(120), nullable=False)
    deleted_at: datetime = db.Column(db.DatetTime, nullable=False)

