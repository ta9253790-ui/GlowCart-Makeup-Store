# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from .models import Product
from django.db.models import Q
from .models import Product, Category, Order
from .models import Product, Category, Order, Review
from django.contrib.auth.decorators import login_required


def home(request):

    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(
            Q(name__icontains=query)
        )
    else:    
        products = Product.objects.all()

    return render(request, 'home.html', {
        'products': products
    })


# Add To Cart
def add_to_cart(request, product_id):

    product = get_object_or_404(Product, id=product_id)

    cart = request.session.get('cart', [])

    found = False

    for item in cart:

        if item['id'] == product.id:
            item['quantity'] += 1
            found = True
            break

    if not found:

        cart.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'image': product.image.url,
            'quantity': 1
        })

    request.session['cart'] = cart

    return redirect('cart')


# Cart Page
def cart(request):

    cart_items = request.session.get('cart', [])

    total = 0

    for item in cart_items:
        total += item['price'] * item['quantity']

    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'total': total
    })


# Increase Quantity
def increase_quantity(request, product_id):

    cart = request.session.get('cart', [])

    for item in cart:

        if item['id'] == product_id:
            item['quantity'] += 1
            break

    request.session['cart'] = cart

    return redirect('cart')


# Decrease Quantity
def decrease_quantity(request, product_id):

    cart = request.session.get('cart', [])

    updated_cart = []

    for item in cart:

        if item['id'] == product_id:

            if item['quantity'] > 1:
                item['quantity'] -= 1
                updated_cart.append(item)

        else:
            updated_cart.append(item)

    request.session['cart'] = updated_cart

    return redirect('cart')


# Remove From Cart
def remove_from_cart(request, product_id):

    cart = request.session.get('cart', [])

    updated_cart = []

    for item in cart:

        if item['id'] != product_id:
            updated_cart.append(item)

    request.session['cart'] = updated_cart

    return redirect('cart')


# Wishlist Page
def wishlist(request):

    wishlist_items = request.session.get('wishlist', [])

    return render(request, 'wishlist.html', {
        'wishlist_items': wishlist_items
    })


# Add To Wishlist
def add_to_wishlist(request, product_id):

    products = Product.objects.all()

    selected_product = None

    for product in products:
        if product.id == product_id:
            selected_product = {
                'id': product.id,
                'name': product.name,
                'price': product.price,
                'image': product.image.url
            }

    wishlist = request.session.get('wishlist', [])

    already_exists = False

    for item in wishlist:
        if item['id'] == product_id:
            already_exists = True

    if not already_exists:
        wishlist.append(selected_product)

    request.session['wishlist'] = wishlist

    return redirect('wishlist')


def remove_from_wishlist(request, product_id):

    wishlist = request.session.get('wishlist', [])

    new_wishlist = []

    for item in wishlist:
        if item['id'] != product_id:
            new_wishlist.append(item)

    request.session['wishlist'] = new_wishlist

    return redirect('wishlist')


# Checkout Page
def checkout(request):

    cart_items = request.session.get('cart', [])

    total = 0

    for item in cart_items:
        total += item['price'] * item['quantity']

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


# Place Order
def place_order(request):

    cart_items = request.session.get('cart', [])

    for item in cart_items:

        cart_items = request.session.get('cart', [])

    for item in cart_items:

        try:

            product = Product.objects.get(id=item['id'])

            Order.objects.create(
                product=product,
                product_name=item['name'],
                price=item['price'],
                quantity=item['quantity'],
                image=item['image']
            )

        except:
            pass

    request.session['cart'] = []

    return redirect('order_success')

def order_history(request):

    orders = Order.objects.all().order_by('-ordered_date')

    return render(request, 'order_history.html', {
        'orders': orders
    })


# Order Success Page
def order_success(request):

    return render(request, 'order_success.html')


# Logout
def logout_view(request):

    logout(request)

    return redirect('home')

from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')

def clear_cart(request):
    request.session['cart'] = []
    return redirect('home')


def product_detail(request, product_id):

    product = Product.objects.get(id=product_id)

    reviews = Review.objects.filter(product=product)

    if request.method == "POST":

        name = request.POST.get('name')

        rating = request.POST.get('rating')

        comment = request.POST.get('comment')

        Review.objects.create(
            product=product,
            name=name,
            rating=rating,
            comment=comment
        )

    return render(request, 'product_detail.html', {
        'product': product,
        'reviews': reviews
    })