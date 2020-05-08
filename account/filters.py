import django_filters
from django_filters import DateFilter, CharFilter

from .models import Order

class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte', label='Starts at')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte', label='ends at')
    
    note = CharFilter(field_name='note', lookup_expr='icontains')

    class Meta:
        model = Order
        fields = '__all__'
        exclude=['customer', 'date_created']