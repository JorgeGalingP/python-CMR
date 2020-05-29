import django_filters

from django import forms
from django_filters import filters

from django.contrib.auth.models import User
from .models import Order, Customer, Product

class OrderFilter(django_filters.FilterSet):
    product = filters.ModelChoiceFilter(
                        queryset=Product.objects.all(),
                        empty_label="Search by product...",
                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    status = filters.ChoiceFilter(
                        choices=Order.STATUS,
                        empty_label="Search by order's status...",
                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    note = filters.CharFilter(
                        field_name='note', 
                        lookup_expr='icontains', 
                        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    start_date = filters.DateFilter(
                        field_name='date_created', 
                        lookup_expr='gte', 
                        label='Starts at', 
                        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    end_date = filters.DateFilter(
                        field_name='date_created', 
                        lookup_expr='lte', 
                        label='ends at', 
                        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    
    class Meta:
        model = Order
        fields = '__all__'
        exclude=['customer', 'date_created']


class CustomerFilter(django_filters.FilterSet):
    user = filters.ModelChoiceFilter(
                        queryset=User.objects.all(),
                        empty_label="Search by an user...",
                        widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    email = filters.CharFilter(
                        field_name='email', 
                        lookup_expr='icontains',
                        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Customer
        fields = '__all__'
        exclude=['name', 'phone', 'date_created']