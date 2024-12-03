from app.models import Payment
from app import db
from typing import List

class PaymentRepository:

  def all(self) -> List[Payment]:
      stocks = db.session.query(Payment).all()
      return stocks

  def save(self, payment: Payment) -> Payment:
      db.session.add(payment)
      db.session.commit()
      return payment
  
