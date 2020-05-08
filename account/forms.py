from django.forms import ModelForm, HiddenInput
from .models import Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True

    class Meta:
        model = Order
        fields = '__all__' # ['product', 'status', 'note'] for all attributes
        widgets = {
            'customer': HiddenInput(),
        }