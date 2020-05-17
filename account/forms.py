from django.forms import ModelForm, HiddenInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order

class OrderForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': HiddenInput(),
        }


class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email=forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), 
        max_length=64, 
        help_text='Enter a valid email address.')
    password1=forms.CharField(
        label= ('Password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text='Your password can’t be too similar to your other personal information, must contain at least 8 characters, can’t be a commonly used password and can’t be entirely numeric.')
    password2=forms.CharField(
        label= ('Repeat password'),
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']