from django.urls import path

from . import views


app_name = "shoppingcart"

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/', views.cart, name='cart'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='details'),
]
