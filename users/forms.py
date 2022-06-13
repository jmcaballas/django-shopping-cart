from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ['email',
            'username',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'billing_street',
            'billing_city',
            'billing_postal',
            'shipping_street',
            'shipping_city',
            'shipping_postal',
            'phone',
        ]
