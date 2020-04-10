from django.shortcuts import render
from items.models import Item

# Create your views here.
def product_list(request):
    products = Item.objects.all().order_by("title")
    return render(request, 'products/product_list.html', {'products': products})