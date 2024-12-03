from app.models import Stock
from app import db
from typing import List
from sqlalchemy import func

class StockRepository:

  def all(self) -> List[Stock]:
      stocks = db.session.query(Stock).all()
      return stocks

  def save(self, stock: Stock) -> Stock:
      db.session.add(stock)
      db.session.commit()
      return stock
  
  def calcular_stock(self, producto_id: int):
    stock_total = (
        db.session.query(
            func.sum(Stock.cantidad * Stock.entrada_salida)
        )
        .filter(Stock.producto_id == producto_id)
        .scalar()
    )
    return stock_total if stock_total is not None else 0