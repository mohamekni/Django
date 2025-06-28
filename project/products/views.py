from django.shortcuts import render
from .models import Product
# Create your views here.

def product(request):
    return render(request, 'products/product.html')

def products(request):

    # get(id=1)
    # all()
    # filter(price=850)
    # order_by('price')
    # count()
    # exclude(price=850)
    # filter(price__exact=850)
    # filter(name__contains='pro')
    # filter(price__in=[850, 999])
    # filter(price__range=[900, 1000])

    all_Items = Product.objects.all()
    items = {'products': all_Items.filter(price__range=[900, 1000])}
    return render(request, 'products/products.html', items)