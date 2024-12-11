from dataclasses import dataclass

from ..models import Product, Compra


@dataclass
class Carrito:
    producto_id: Product
    direccion_envio: str
    cantidad: float
    medio_pago: str
