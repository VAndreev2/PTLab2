from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase, CartItem


# Главная страница с товарами
def index(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_items = [
        {'product': Product.objects.get(id=int(product_id)),}
        for product_id in cart
    ]
    total_price = sum(item['product'].price for item in cart_items)
    context = {
        'products': products,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/index.html', context)

# Добавить товар в корзину
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    # Добавляем товар в корзину, если его там нет
    if str(product_id) not in cart:
        cart[str(product_id)] = 1  # Устанавливаем количество товара как 1

    request.session['cart'] = cart
    return redirect('index')

# Удалить товар из корзины
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('index')


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['person', 'address']

    def dispatch(self, request, *args, **kwargs):
        # Получаем cart из сессии
        self.cart = request.session.get('cart', {})
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Проверка наличия товаров в корзине
        if not self.cart:
            return HttpResponse("Корзина пуста.", status=400)

        # Сохраняем объект Purchase
        form.instance.total_cost = sum(
            Product.objects.get(id=int(product_id)).price
            for product_id in self.cart.keys()
        )
        self.object = form.save()  # Сохраняем объект в базе данных

        # Создаем записи в CartItem для каждого товара в корзине
        for product_id in self.cart.keys():
            product = Product.objects.get(id=int(product_id))
            CartItem.objects.create(product=product, purchase=self.object)

        # Очищаем корзину в сессии
        self.request.session['cart'] = {}

        # Форматируем дату без времени
        formatted_date = self.object.date.strftime('%b %d, %Y')  # Например, "Nov 07, 2024"
        information = {
            'id': self.object.id,  # ID записи
            'date': formatted_date,  # Дата создания записи
            'total_cost': self.object.total_cost,  # Общая стоимость
        }
        # Возвращаем ответ
        return render(self.request, 'shop/success.html', information)

