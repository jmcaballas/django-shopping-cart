from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def home(request):
    return render(request, 'shoppingcart/home.html', {})

@login_required
def cart(request):
    return render(request, 'shoppingcart/cart.html', {})
