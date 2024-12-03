from app.models import Compra
from app import db


class CompraRepository:

  def save(self, compra: Compra) -> Compra:
    db.sessions.add(compra)
    db.session.commit()
    return compra

