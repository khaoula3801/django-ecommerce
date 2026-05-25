from .models import Product, Category, Cart, CartItem
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


def get_or_create_cart(user):
    cart, _ = Cart.objects.get_or_create(user=user)
    return cart


@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart = get_or_create_cart(request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')


@login_required
def cart(request):
    cart = get_or_create_cart(request.user)
    cart_items = cart.items.select_related('product').all()
    total = cart.get_total()

    return render(request, 'products/cart.html', {
        'cart_items': cart_items,
        'total': total
    })


@login_required
def remove_from_cart(request, id):
    cart = get_or_create_cart(request.user)
    cart_item = get_object_or_404(CartItem, id=id, cart=cart)
    cart_item.delete()
    return redirect('cart')


@login_required
def decrease_quantity(request, id):
    """Diminue la quantité de 1, supprime l'article si quantité = 0"""
    cart = get_or_create_cart(request.user)
    cart_item = get_object_or_404(CartItem, id=id, cart=cart)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')


@login_required
def increase_quantity(request, id):
    """Augmente la quantité de 1"""
    cart = get_or_create_cart(request.user)
    cart_item = get_object_or_404(CartItem, id=id, cart=cart)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'products/product_detail.html', {'product': product})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'products/category_list.html', {'categories': categories})

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = category.products.all()
    return render(request, 'products/category_detail.html', {
        'category': category,
        'products': products
    })

def home(request):
    return render(request, 'home.html')