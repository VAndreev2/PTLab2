from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['person', 'address']

    def dispatch(self, request, *args, **kwargs):
        # Получаем product_ids из URL
        self.product = self.request.POST.get('product_ids')
        self.total_cost = self.request.POST.get('total_cost')  # total_cost
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Проверка наличия product_ids
        if not self.product:
            return HttpResponse("Не указаны товары для покупки.", status=400)

        # Заполняем поле product_ids в форме
        form.instance.product = self.product  # Сохраняем список продуктов как строку
        form.instance.total_cost = self.total_cost
        self.object = form.save()  # Сохраняем объект в базе данных

        # Форматируем дату без времени
        formatted_date = self.object.date.strftime('%b %d, %Y')  # Например, "Nov 07, 2024"
        information = {
            'id': self.object.id,  # ID записи
            'date': formatted_date,  # Дата создания записи
            'total_cost': self.object.total_cost,  # Общая стоимость
        }
        # Возвращаем ответ
        return render(self.request, 'shop/success.html', information)

