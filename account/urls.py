from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="account_home"),
    path('products/', views.products, name="account_products"),
    path('customer/<str:customer_pk>', views.customer, name="account_customer"),
]
