from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Product


def home(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    
    return render(request, 'shoppingcart/home.html', context)

@login_required
def cart(request):
    return render(request, 'shoppingcart/cart.html', {})
