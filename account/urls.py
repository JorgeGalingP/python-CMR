from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="account_home"),
    
    path('login/', views.login, name="account_login"),
    path('register/', views.register, name="account_register"),
    
    path('customer/<str:customer_pk>', views.customer, name="account_customer"),
    path('customers/', views.all_customers, name="account_customers"),
    
    path('products/', views.all_products, name="account_products"),
    
    path('orders/', views.all_orders, name="account_orders"),
    path('createOrder/<str:customer_pk>', views.create_order, name="account_create_order"),
    path('updateOrder/<str:order_pk>', views.update_order, name="account_update_order"),
    path('deleteOrder/<str:order_pk>', views.delete_order, name="account_delete_order"),
]
