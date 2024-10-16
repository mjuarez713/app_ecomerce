from dataclasses import dataclass
from app import db

@dataclass
class Product(db.Model):
    __tablename__ = 'product'
    id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(120), nullable=False)
    price: float = db.Column(db.Float, nullable=False)
    #stock = stock

    def __init__(self, name: int, price:float):
        self.name = name
        self.price = price
