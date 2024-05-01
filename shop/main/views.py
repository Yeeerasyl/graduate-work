from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import render, get_object_or_404



def index(request):
    selected_sort = request.GET.get('sort', 'default')

    if selected_sort == 'price_asc':
        products = Product.objects.order_by('price')
    elif selected_sort == 'price_desc':
        products = Product.objects.order_by('-price')
    else:
        products = Product.objects.all()

    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'product': products, 'selected_sort': selected_sort})

def about(request):
    return render(request,'main/about.html')

def product(request):
    return render(request,'main/product')

def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'main/index.html', {'product': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'main/product_detail.html', {'product': product})