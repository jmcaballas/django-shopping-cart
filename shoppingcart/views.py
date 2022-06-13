from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def shoppingcart(request):
    return render(request, 'shoppingcart/home.html', {})
