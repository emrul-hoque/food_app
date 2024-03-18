from django.shortcuts import render, redirect
from .models import Product, Order
from django.http import HttpResponse
import random

def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)

def place_order(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        quantity = int(request.POST['quantity'])
        delivery_address = request.POST['delivery_address']
        product = Product.objects.get(pk=product_id)
        total_price = product.price * quantity
        order = Order.objects.create(product=product, quantity=quantity, total_price=total_price, delivery_address=delivery_address)
        return redirect('home')
    else:
        return redirect('home')


def display_products(request):
    # Retrieve all products from the database
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def place_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity'))
        total_amount = calculate_total_amount(product_id, quantity)
        
        delivery_time = random.randint(15, 30)

        return render(request, 'order_summary.html', {'total_amount': total_amount, 'delivery_time': delivery_time})

def calculate_total_amount(product_id, quantity):
   
    total_amount = 0 
    return total_amount
