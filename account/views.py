from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from .models import Order, Customer, Product, Video
from .forms import OrderForm, CreateUserForm, AuthenticationAccountForm
from .filters import OrderFilter, CustomerFilter


def login_page(request):
    form = AuthenticationAccountForm()
    err = False
    context = {'form': form}

    if request.method == 'POST':
        form = AuthenticationAccountForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('account_home')
            else:
                err = True
                messages.info(request, 'Username or password is incorrect')
        else:
                err = True
                messages.info(request, 'Username or password is invalid')
                

    if err:
        return render(request, 'account/login.html', context)

    return render(request, 'account/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('account_login')


def register_page(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account was created ', username)

            return redirect('account_login')

    context = {'form': form}

    return render(request, 'account/register.html', context)


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


def all_products(request):
    products = Product.objects.all()

    context = {'products': products}

    return render(request, 'account/all_products.html', context)


def all_customers(request):
    customers = Customer.objects.all()

    filter = CustomerFilter(request.GET, queryset=customers)
    customers_filtered = filter.qs

    context = {'customers': customers_filtered, 'filter': filter}

    return render(request, 'account/all_customers.html', context)


def all_videos(request):
    videos = Video.objects.all()

    context = {'videos': videos}

    return render(request, 'account/all_videos.html', context)


def all_orders(request):
    orders = Order.objects.all()

    filter = OrderFilter(request.GET, queryset=orders)
    orders_filtered = filter.qs

    paginator = Paginator(orders_filtered, 10)
    page = request.GET.get('page')
    orders_paginated = paginator.get_page(page)

    context = {'orders': orders_paginated, 'filter': filter}

    return render(request, 'account/all_orders.html', context)


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
            return redirect('account_home')

    context = {'form': form}
    return render(request, 'account/order_form.html', context)


def update_order(request, order_pk):
    order = Order.objects.get(id=order_pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order) 

        if form.is_valid():
            form.save()
            return redirect('account_home')

    context = {'form': form}
    return render(request, 'account/order_form.html', context) 


def delete_order(request, order_pk):
    order = Order.objects.get(id=order_pk)
    
    if request.method == 'POST':
        order.delete()
        return redirect('account_home')

    context = {'item': order}
    return render(request, 'account/delete.html', context)


