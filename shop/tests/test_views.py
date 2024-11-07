from django.urls import reverse
from django.test import TestCase, Client

from shop.models import Purchase, Product

class PurchaseCreateTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.product_book = Product.objects.create(name="book", price=740)
        self.product_pencil = Product.objects.create(name="pencil", price=20)
        self.product_ruler = Product.objects.create(name="ruler", price=30)

    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_purchase_creation_valid(self):
        response = self.client.post(reverse('buy', args=[self.product_book.id]), {
            'person': 'John Doe',
            'address': '123 Elm Street',
            'product_ids': self.product_book.id,  # Товары, которые покупает пользователь
            'total_cost': self.product_book.price
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Спасибо за покупку', response.content.decode())
        self.assertEqual(Purchase.objects.count(), 1)  # Проверяем, что объект Purchase был создан

    def test_purchase_with_many_products(self):
        self.url_ids = f"{self.product_book.id},{self.product_pencil.id},{self.product_ruler.id}"
        response = self.client.post(reverse('buy', args=[self.url_ids]), {
            'person': 'John Doe',
            'address': '123 Elm Street',
            'product_ids': self.url_ids,  # Товары, которые покупает пользователь
            'total_cost': self.product_book.price+self.product_pencil.price+self.product_ruler.price
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Спасибо за покупку', response.content.decode())
        self.assertEqual(Purchase.objects.count(), 1)  # Проверяем, что объект Purchase был создан
