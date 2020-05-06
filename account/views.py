from django.shortcuts import render
from django.http import HttpResponse
from .models import Order, Customer, Product

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 
        'customers': customers,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending}

    return render(request, 'account/dashboard.html', context)

def products(request):
    products = Product.objects.all()

    return render(request, 'account/products.html', {'products': products})

def customer(request, customer_pk):
    customer = Customer.objects.get(id=customer_pk)

    orders = customer.order_set.all()

    total_orders = orders.count()

    context = {'customer': customer, 'orders': orders, 'total_orders': total_orders}

    return render(request, 'account/customer.html', context)

