from typing import List#, Type
from app.models import Product
from app import db

class ProductRepository:
    
    def save(self, product: Product) -> Product:
        db.session.add(product)
        db.session.commit()
        return product

    def all(self) -> List[Product]:
        """Obtiene todos los productos de la base de datos."""
        products = db.session.query(Product).all()
        return products

    def find(self, id: int) -> Product:
        """Encuentra un producto por su ID."""
        if id is None or id == 0:
            return None 
        try:
            return db.session.query(Product).filter(Product.id == id).one()
        except:
            return None

    def find_by_name(self, name: str) -> Product: 
        """Encuentra un producto por su nombre."""
        return db.session.query(Product).filter(Product.name == name).one_or_none()
