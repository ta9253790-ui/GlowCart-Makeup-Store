from django.urls import path
from . import views

urlpatterns = [

    path('', views.login_view, name='login'),

    path('home/', views.home, name='home'),

    path('cart/', views.cart, name='cart'),

    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),

    path('increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),

    path('decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),

    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('wishlist/', views.wishlist, name='wishlist'),

    path('add-to-wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),

    path('remove-wishlist/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

    path('checkout/', views.checkout, name='checkout'),

    path('place-order/', views.place_order, name='place_order'),

    path('order-success/', views.order_success, name='order_success'),

    path('logout/', views.logout_view, name='logout'),

    path('orders/', views.order_history, name='order_history'),

    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]