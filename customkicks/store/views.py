from django.shortcuts import render
from .models import Product

# home page Route/View
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products':products})