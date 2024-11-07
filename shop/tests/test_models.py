import sys, os
from django.test import TestCase
from shop.models import Product, Purchase
from datetime import datetime

class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="book", price="740")
        Product.objects.create(name="pencil", price="50")

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(name="book").name, str)
        self.assertIsInstance(Product.objects.get(name="book").price, int)
        self.assertIsInstance(Product.objects.get(name="pencil").name, str)
        self.assertIsInstance(Product.objects.get(name="pencil").price, int)

    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(name="book").price == 740)
        self.assertTrue(Product.objects.get(name="pencil").price == 50)

    def test_create_and_delete_product(self):
        product = Product.objects.create(name="temp_product", price="100")
        self.assertIsNotNone(product.id)
        product.delete()
        with self.assertRaises(Product.DoesNotExist):
            Product.objects.get(id=product.id)

    def test_update_product(self):
        product = Product.objects.get(name="book")
        product.price = "800"
        product.save()
        self.assertEqual(Product.objects.get(name="book").price, 800)


class PurchaseTestCase(TestCase):
    def setUp(self):
        self.product_book = Product.objects.create(name="book", price="740")
        self.datetime = datetime.now()
        Purchase.objects.create(product=self.product_book,
                                person="Ivanov",
                                address="Svetlaya St.",
                                total_cost=2000)

    def test_correctness_types(self):
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).person, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).address, str)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).date, datetime)
        self.assertIsInstance(Purchase.objects.get(product=self.product_book).total_cost, int)

    def test_correctness_data(self):
        self.assertTrue(Purchase.objects.get(product=self.product_book).person == "Ivanov")
        self.assertTrue(Purchase.objects.get(product=self.product_book).address == "Svetlaya St.")
        self.assertTrue(Purchase.objects.get(product=self.product_book).date.replace(microsecond=0) == \
            self.datetime.replace(microsecond=0))
        self.assertTrue(Purchase.objects.get(product=self.product_book).total_cost == 2000)

    def test_required_fields(self):
        with self.assertRaises(Exception):
            Purchase.objects.create(product=self.product_book, person="", address="")