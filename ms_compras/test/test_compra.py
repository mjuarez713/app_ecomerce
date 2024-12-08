import unittest
from flask import current_app
from app import create_app, db
from app.models import Compra
from app.services import CompraService

"""
class CompraTestCase(unittest.TestCase):

    def setUp(self):       
        self.NAME_PRUEBA = 'silla'
        self.PRICE_PRUEBA = 700.5
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.product_services = ProductService()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app(self):
        self.assertIsNotNone(current_app)
    
    def test_product(self):
        product = self.__get_product()
        self.assertTrue(product.name, self.NAME_PRUEBA)
        self.assertTrue(product.price, self.PRICE_PRUEBA)

    def test_product_all(self):
        product = self.__get_product()
        self.product_services.save(product)
        products = self.product_services.all()
        self.assertGreaterEqual(len(products), 1)
    
    def __get_product(self):
        product = Product()
        product.name=self.NAME_PRUEBA,
        product.price=self.PRICE_PRUEBA,
        return product

if __name__ == '__main__':
    unittest.main()



    


"""