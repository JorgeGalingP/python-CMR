from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [    
    path('register/', views.register_page, name="account_register"),
    path('login/', views.login_page, name="account_login"),
    path('logout/', views.logout_page, name="account_logout"),

    path('', views.home, name="account_home"),

    path('user/', views.user, name="account_user"),
    path('userSettings/', views.user_settings, name="account_user_settings"),
    
    path('customer/<str:customer_pk>', views.customer, name="account_customer"),
    path('customers/', views.all_customers, name="account_customers"),
    
    path('products/', views.all_products, name="account_products"),

    path('videos/', views.all_videos, name="account_videos"),
    
    path('orders/', views.all_orders, name="account_orders"),
    path('createOrder/<str:customer_pk>', views.create_order, name="account_create_order"),
    path('updateOrder/<str:order_pk>', views.update_order, name="account_update_order"),
    path('deleteOrder/<str:order_pk>', views.delete_order, name="account_delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="account/password_reset.html"), name="password_reset"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="account/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="account/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="account/password_reset_complete.html"), name="password_reset_complete"),
]
