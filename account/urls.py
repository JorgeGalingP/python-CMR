from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="account_home"),
    path('products/', views.products, name="account_products"),
    path('customer/<str:customer_pk>', views.customer, name="account_customer"),
    path('createOrder/', views.create_order, name="account_create_order"),
    path('updateOrder/<str:order_pk>', views.update_order, name="account_update_order"),
    path('deleteOrder/<str:order_pk>', views.delete_order, name="account_delete_order"),
]
