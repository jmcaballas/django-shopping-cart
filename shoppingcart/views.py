from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import Product, SaleOrder, SaleOrderItem, ProductImage


class ProductListView(ListView):
    queryset = Product.objects.with_stock()
    template_name = "shoppingcart/home.html"
    context_object_name = 'products'
    ordering = ['name']
    paginate_by = 24

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            cart_count = SaleOrderItem.objects.filter(sale_order__user=self.request.user).count()
            context["cart_count"] = cart_count
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.with_stock()
    model = ProductImage
    template_name = "shoppingcart/details.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if self.request.user.is_authenticated:
            cart_count = SaleOrderItem.objects.filter(sale_order__user=self.request.user).count()
            context["cart_count"] = cart_count
        
        product_image = ProductImage.objects.filter(product__name=self.object.name)
        context["product_image"] = product_image
        
        return context


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
    return redirect('shoppingcart:cart')


@login_required
def delete_from_cart(request, id):
    delete_product = SaleOrderItem.objects.filter(sale_order__user=request.user, id=id)
    if delete_product.exists():
        delete_product[0].delete()

    cart_count = SaleOrderItem.objects.filter(sale_order__user=request.user).count()

    if cart_count == 0:
        SaleOrder.objects.filter(user=request.user).delete()
    return redirect('shoppingcart:cart')


@login_required
def cart(request):
    sales = SaleOrderItem.objects.filter(sale_order__user=request.user)
    cart_count = SaleOrderItem.objects.filter(sale_order__user=request.user).count()
    cart_total = SaleOrderItem.objects.filter(sale_order__user=request.user).aggregate(Sum('unit_price'))['unit_price__sum']

    context = {
        'sales': sales,
        'cart_count': cart_count,
        'cart_total': cart_total,
    }

    return render(request, 'shoppingcart/cart.html', context)


@login_required
def checkout(request):
    checkout_product = SaleOrderItem.objects.filter(sale_order__user=request.user)
    
    if checkout_product.exists():
        checkout_product.delete()

    cart_count = SaleOrderItem.objects.filter(sale_order__user=request.user).count()

    if cart_count == 0:
        SaleOrder.objects.filter(user=request.user).delete()
    
    context = {
        'cart_count': cart_count,
    }

    return render(request, 'shoppingcart/checkout.html', context)