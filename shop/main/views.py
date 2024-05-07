from django.shortcuts import render
from .models import Product,Category
from django.shortcuts import render, get_object_or_404

from ultralytics import YOLO
import cv2
import re

model = YOLO("C:\\Users\\yeras\\OneDrive\\Документы\\GitHub\\graduate-work\\shop\\main\\best.pt")

def handle_uploaded_file(f):
    with open (f"uploads/{f.name}","wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def process_image(image_path):
    im1 = cv2.imread(image_path)
    results = model.predict(source=im1)
    final_result = results[0].verbose()
    predictions_list = final_result.split(", ")
    first_prediction = predictions_list[0]
    first_prediction = re.sub(r'[\d\.]+', '', first_prediction)
    return first_prediction

def index(request):
    selected_sort = request.GET.get('sort', 'default')

    if selected_sort == 'price_asc':
        products = Product.objects.order_by('price')
    elif selected_sort == 'price_desc':
        products = Product.objects.order_by('-price')
    else:
        products = Product.objects.all()

    if request.method == 'POST' and request.FILES.get('file_upload'):
        handle_uploaded_file(request.FILES['file_upload'])
        image_path = f"uploads/{request.FILES['file_upload'].name}"
        prediction = process_image(image_path)
        print(prediction)  

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