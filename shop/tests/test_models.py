import sys, os

from django.test import TestCase
from shop.models import Product, Purchase, CartItem
from datetime import datetime, timedelta

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
        Purchase.objects.create(person="Ivanov",
                                address="Svetlaya St.",
                                date=self.datetime,
                                total_cost=2000)

    def test_correctness_types(self):
        purchase = Purchase.objects.get(person="Ivanov")
        self.assertIsInstance(purchase.person, str)
        self.assertIsInstance(purchase.address, str)
        self.assertIsInstance(purchase.date, datetime)
        self.assertIsInstance(purchase.total_cost, int)

    def test_correctness_data(self):
        purchase = Purchase.objects.get(person="Ivanov")
        self.assertEqual(purchase.person, "Ivanov")
        self.assertEqual(purchase.address, "Svetlaya St.")
        self.assertEqual(purchase.total_cost, 2000)

    def test_create_and_delete_purchase(self):
        purchase = Purchase.objects.create(
            person="Petrov",
            address="Temnaya St.",
            date=datetime.now(),
            total_cost=1500
        )
        self.assertIsNotNone(purchase.id)
        purchase.delete()
        with self.assertRaises(Purchase.DoesNotExist):
            Purchase.objects.get(id=purchase.id)

    def test_update_purchase(self):
        purchase = Purchase.objects.get(person="Ivanov")
        purchase.total_cost = 2500
        purchase.save()
        self.assertEqual(Purchase.objects.get(person="Ivanov").total_cost, 2500)

class CartItemTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="book", price=740)
        self.purchase = Purchase.objects.create(
            person="Ivanov",
            address="Svetlaya St.",
            date=datetime.now(),
            total_cost=2000
        )
        self.cart_item = CartItem.objects.create(
            product=self.product,
            purchase=self.purchase
        )

    def test_correctness_types(self):
        cart_item = CartItem.objects.get(product=self.product, purchase=self.purchase)
        self.assertIsInstance(cart_item.product, Product)
        self.assertIsInstance(cart_item.purchase, Purchase)

    def test_correctness_data(self):
        cart_item = CartItem.objects.get(product=self.product, purchase=self.purchase)
        self.assertEqual(cart_item.product, self.product)
        self.assertEqual(cart_item.purchase, self.purchase)

    def test_create_and_delete_cart_item(self):
        cart_item = CartItem.objects.create(
            product=self.product,
            purchase=self.purchase
        )
        self.assertIsNotNone(cart_item.id)
        cart_item.delete()
        with self.assertRaises(CartItem.DoesNotExist):
            CartItem.objects.get(id=cart_item.id)

    def test_update_cart_item(self):
        new_product = Product.objects.create(name="pencil", price=50)
        cart_item = CartItem.objects.get(product=self.product, purchase=self.purchase)
        cart_item.product = new_product
        cart_item.save()
        updated_cart_item = CartItem.objects.get(id=cart_item.id)
        self.assertEqual(updated_cart_item.product, new_product)