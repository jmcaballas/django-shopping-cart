from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# @login_required
def home(request):
    return render(request, 'shoppingcart/home.html', {})

def cart(request):
    return render(request, 'shoppingcart/cart.html', {})
