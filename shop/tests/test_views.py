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
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        # Добавляем товар в корзину
        response = self.client.post(reverse('add_to_cart', args=[self.product_book.id]))
        self.assertEqual(response.status_code, 302)  # Ожидаем перенаправление
        self.assertIn('cart', self.client.session)
        self.assertEqual(self.client.session['cart'][str(self.product_book.id)], 1)

    def test_add_to_cart_double(self):
        response = self.client.post(reverse('add_to_cart', args=[self.product_book.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('cart', self.client.session)
        response = self.client.post(reverse('add_to_cart', args=[self.product_book.id]))
        self.assertEqual(response.status_code, 302)  # Ожидаем перенаправление
        self.assertIn('cart', self.client.session)
        self.assertEqual(self.client.session['cart'][str(self.product_book.id)], 1)

    def test_purchase_creation_valid(self):
        # Добавляем товар в корзину
        self.client.post(reverse('add_to_cart', args=[self.product_book.id]))

        # Создаем объект Purchase
        response = self.client.post(reverse('purchase'), {
            'person': 'John Doe',
            'address': '123 Elm Street',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Purchase.objects.count(), 1)  # Проверяем, что объект Purchase был создан

        purchase = Purchase.objects.first()
        self.assertEqual(purchase.person, 'John Doe')
        self.assertEqual(purchase.address, '123 Elm Street')
        self.assertEqual(purchase.total_cost, self.product_book.price)
