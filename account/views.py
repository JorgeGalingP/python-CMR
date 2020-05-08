from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Order, Customer, Product
from .forms import OrderForm
from .filters import OrderFilter


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders[:5], 
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

    filter = OrderFilter(request.GET, queryset=orders)
    orders_filtered = filter.qs

    context = {'customer': customer, 'orders': orders_filtered, 'total_orders': total_orders, 'filter': filter}

    return render(request, 'account/customer.html', context)


def create_order(request, customer_pk):
    customer = Customer.objects.get(id=customer_pk)
    form = OrderForm(initial={'customer': customer})  

    if request.method == 'POST':
        form = OrderForm(request.POST, initial={'customer': customer})

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/order_form.html', context)


def update_order(request, order_pk):
    order = Order.objects.get(id=order_pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order) 

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'account/order_form.html', context) 


def delete_order(request, order_pk):
    order = Order.objects.get(id=order_pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'item': order}
    return render(request, 'account/delete.html', context)


