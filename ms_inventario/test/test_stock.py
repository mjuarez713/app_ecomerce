import unittest
from flask import current_app
from app import create_app, db
from app.models import Stock


class StockTestCase(unittest.TestCase):

  """
  The setUp() and tearDown() methods allow you to define instructions 
  that will be executed before and after each test method
  """

  def setUp(self):
    self.PRODUCTO = 1
    self.CANTIDAD = 10
    self.ENTRADA_SALIDA = 1

    self.app = create_app()
    self.app_context = self.app.app_context()
    self.app_context.push()
    db.create_all()
    
  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()
  
  def test_stock(self):
    stock = self.__get_stock()
    self.assertEqual(stock.producto_id, self.PRODUCTO)
    self.assertIsNotNone(stock.fecha_transaccion)
    self.assertEqual(stock.cantidad, self.CANTIDAD)
    self.assertEqual(stock.entrada_salida, self.ENTRADA_SALIDA)
    

  def __get_stock(self): 
    stock = Stock()
    stock.producto_id = self.PRODUCTO
    stock.cantidad = self.CANTIDAD
    stock.entrada_salida = self.ENTRADA_SALIDA
    return stock

if __name__ == '__main__':
    unittest.main()