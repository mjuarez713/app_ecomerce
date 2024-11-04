from app.models import Stock
from app import db
from typing import List

class StockRepository:

  def all(self) -> List[Stock]:
      stocks = db.session.query(Stock).all()
      return stocks

  def save(self, stock: Stock) -> Stock:
      db.session.add(stock)
      db.session.commit()
      return stock