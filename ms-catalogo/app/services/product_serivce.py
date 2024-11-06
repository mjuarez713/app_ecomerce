from typing import List
from app.models import Product
from app.repositories import ProductRepository

repository = ProductRepository()

class ProductService:
    def all(self) -> List[Product]:
        """Obtiene todos los productos."""
        return repository.all()

    def find(self, id: int) -> Product:
        """Encuentra un producto por su ID."""
        return repository.find(id)

    def find_by_name(self, name: str) -> Product:
        """Encuentra un producto por su nombre."""
        return repository.find_by_name(name)
