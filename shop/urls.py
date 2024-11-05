from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/<str:product_ids>/', views.PurchaseCreate.as_view(), name='buy'),
]