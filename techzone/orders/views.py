from django.shortcuts import render, get_object_or_404
from .models import Order
from django.shortcuts import render


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})
from django.shortcuts import render
from .models import Order

def order_history(request):
    orders = Order.objects.filter(customer=request.user.customer).order_by('-order_date')
    return render(request, 'orders/order_history.html', {'orders': orders})
