from dataclasses import dataclass

@dataclass(repr=True, eq=True)
class Product:
    id: int 
    nombre: str
    precio: float
    state: bool
