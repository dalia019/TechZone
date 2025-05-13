from decimal import Decimal
from django.shortcuts import render
from .models import Product

# Create your views here.

def shop(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/shop.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product,
        'discount_price': Decimal(product.product_price) * Decimal(0.9),
        'saved_amount': Decimal(product.product_price) * Decimal(0.1),  
        'feature_list': product.get_feature_list(),
        'colors': product.available_colors.all(),
        'storages': product.available_storage.all(),
        'product_category': product.product_category,
    }
    return render(request, 'products/product-detail.html', context)

def category(request, category_name):
    products = Product.objects.filter(product_category=category_name)
    context = {
        'products': products,
        'category_name': category_name
    }
    return render(request, 'products/category.html', context)


