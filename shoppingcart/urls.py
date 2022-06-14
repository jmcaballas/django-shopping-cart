from django.urls import path

from . import views


app_name = "shoppingcart"

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('cart/add/<slug:slug>', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.cart, name='cart'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
]
