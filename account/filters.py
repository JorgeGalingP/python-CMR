import django_filters
from django_filters import DateFilter, CharFilter

from .models import Order, Customer

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Starts at')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='ends at')
    
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude=['customer', 'date_created']


class CustomerFilter(django_filters.FilterSet):
    email = CharFilter(field_name='email', lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = '__all__'
        exclude=['name', 'phone', 'date_created']