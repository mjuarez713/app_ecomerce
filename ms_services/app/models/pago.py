from dataclasses import dataclass
import datetime

@dataclass(init=False, repr=True, eq=True)
class Payment:
    id: int
    producto_id: int
    precio: float
    medio_de_pago: str
