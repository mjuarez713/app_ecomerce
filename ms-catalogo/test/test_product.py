import unittest
from flask import current_app
from app import create_app, db
from app.models import Product
from app.services import ProductService

class ProductTestCase(unittest.TestCase):

    def setUp(self):       
        self.NAME_PRUEBA = 'silla'
        self.PRICE_PRUEBA = 700.5
        self.product_services = ProductService()

        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_product(self):
        product = self.__get_product()
        self.assertEqual(product.name, self.NAME_PRUEBA)
        self.assertEqual(product.price, self.PRICE_PRUEBA)
    
    def __get_product(self):
        product = Product(name=self.NAME_PRUEBA, price=self.PRICE_PRUEBA)
        return product

if __name__ == '__main__':
    unittest.main()



    


