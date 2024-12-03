from app.models import Payment
from typing import List
from app.repositories import PaymentRepository

from datetime import datetime

repository = PaymentRepository()

class StockService:

  def all(self) -> List[Payment]:
    return repository.all()
  
  def save(self, payment) -> Payment:
    result = repository.save(payment)
    return result