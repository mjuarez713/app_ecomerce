from app.models import Stock
from typing import List
from app.repositories import StockRepository

from datetime import datetime

repository = StockRepository()

class StockService:

  def all(self) -> List[Stock]:
    return repository.all()

  def ingreso(self, stock: Stock) -> Stock:
    result = None
    if stock is not None:
      stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
      stock.entrada_salida = 1
      result = repository.save(stock)
    return result


  def egreso(self, stock: Stock) -> Stock:
        result = None
        if stock is not None:
            # Verificar el stock actual
            stock_actual = self.calcular_stock(stock.producto_id)
            if stock_actual <= 0:
                raise ValueError("No se puede realizar el egreso porque el stock es 0 o insuficiente.")
            
            # Configurar los valores y guardar el egreso
            stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
            stock.entrada_salida = -1
            result = repository.save(stock)
        return result
  
  
  def calcular_stock(self, producto_id: int):
    return repository.calcular_stock(producto_id)






#leer 10000 if
#operador ternario


