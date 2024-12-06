from django.urls import path

from . import views
from .views import PurchaseCreate

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('purchase/', PurchaseCreate.as_view(), name='purchase'),
]