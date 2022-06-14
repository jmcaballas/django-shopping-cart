from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Product, SaleOrder, SaleOrderItem


class ProductListView(ListView):
    queryset = Product.objects.with_stock()
    template_name = "shoppingcart/home.html"
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 24


class ProductDetailView(DetailView):
    queryset = Product.objects.with_stock()
    template_name = "shoppingcart/details.html"


@login_required
def add_to_cart(request, slug):
    cart_product = Product.objects.get(slug=slug)
    cart_product_stock = Product.objects.with_stock().get(slug=slug).stock
    quantity = 1

    sale_order = SaleOrder.objects.get_or_create(user=request.user)
    sale_order_item = SaleOrderItem.objects.create(
        product=cart_product,
        quantity=quantity,
        sale_order=sale_order[0],
        unit_price=quantity*cart_product.price
    )
    return HttpResponse("Item added to cart", request)


@login_required
def cart(request):
    return render(request, 'shoppingcart/cart.html', {})
