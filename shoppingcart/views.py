from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Product


def home(request):
    products = Product.objects.all().order_by("name")

    context = {
        'products': products,
    }
    
    return render(request, 'shoppingcart/home.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "shoppingcart/details.html"


@login_required
def cart(request):
    return render(request, 'shoppingcart/cart.html', {})
