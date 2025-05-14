from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, Wishlist
from products.models import Product


@login_required
def cart_view(request):
    items = CartItem.objects.filter(customer=request.user)
    return render(request, 'cart/cart.html', {'cart_items': items})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        customer=request.user, product=product,
        defaults={'quantity': 1}
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')


@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, customer=request.user)
    item.delete()
    return redirect('cart')


@login_required
def update_cart_item(request, item_id):
    if request.method == 'POST':
        new_qty = int(request.POST.get('quantity', 1))
        item = get_object_or_404(CartItem, id=item_id, customer=request.user)
        item.quantity = new_qty
        item.save()
    return redirect('cart')


@login_required
def wishlist_view(request):
    items = Wishlist.objects.filter(customer=request.user)
    return render(request, 'cart/wishlist.html', {'wishlist_items': items})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(customer=request.user, product=product)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, item_id):
    item = get_object_or_404(Wishlist, id=item_id, customer=request.user)
    item.delete()
    return redirect('wishlist')
