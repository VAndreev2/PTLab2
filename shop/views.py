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
        self.product_ids = kwargs.get('product_ids')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Проверка наличия product_ids
        if not self.product_ids:
            return HttpResponse("Не указаны товары для покупки.", status=400)

        # Заполняем поле product_ids в форме
        form.instance.product_ids = self.product_ids  # Сохраняем список продуктов как строку
        self.object = form.save()  # Сохраняем объект в базе данных

        # Возвращаем ответ
        return HttpResponse(f'Спасибо за покупку, {form.instance.person}!')

