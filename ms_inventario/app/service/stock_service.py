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
      stock.fecha_transaccion = stock.fecha_transaccion if stock.fecha_transaccion is not None else datetime.now()
      stock.entrada_salida = 2
      result = repository.save(stock)
    return result






#leer 10000 if
#operador ternario


