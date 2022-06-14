from django.urls import path

from . import views


app_name = "shoppingcart"

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('cart/add/<slug:slug>', views.add_to_cart, name='add-to-cart'),
    path('cart/delete/<int:id>', views.delete_from_cart, name='delete-from-cart'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
]
