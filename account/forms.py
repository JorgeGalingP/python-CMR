from django.forms import ModelForm, HiddenInput
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order, Product

class OrderForm(ModelForm):
    product = forms.ModelChoiceField(
                        queryset=Product.objects.all(),
                        empty_label="Select a product...",
                        widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(
                        choices=Order.STATUS, 
                        widget=forms.Select(attrs={'class': 'form-control'}))
    note = forms.CharField(
                        max_length=200,
                        widget=forms.Textarea(attrs={'class':'form-control'}),
                        help_text='Maximum 200 characters.')

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['customer'].disabled = True

    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'customer': HiddenInput(),
        }
        labels = {
            'product': 'Product',
            'status': 'Status',
            'note': 'Note',
        }


class CreateUserForm(UserCreationForm):
    username = forms.CharField(
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid username'}))
    email=forms.EmailField(
                        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid email'}), 
                        max_length=64, 
                        help_text='Enter a valid email address.')
    password1=forms.CharField(
                        label= ('Password'),
                        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter a valid password'}),
                        help_text='Your password can’t be too similar to your other personal information, must contain at least 8 characters, can’t be a commonly used password and can’t be entirely numeric.')
    password2=forms.CharField(
                        label= ('Repeat password'),
                        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat your password'}),
                        help_text='Enter the same password as before, for verification.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AuthenticationAccountForm(AuthenticationForm):
    username = forms.CharField(
                        label= ('Username'),
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password=forms.CharField(
                        label= ('Password'),
                        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))    

    class Meta:
        model = User
        fields = ['username', 'password']