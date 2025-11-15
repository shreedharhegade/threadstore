from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('product/<int:pk>/', views.product_detail, name="product_detail"),

    # cart
    path('cart/', views.cart_view, name="cart"),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name="add_to_cart"),
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name="remove_from_cart"),

    # checkout
    path('checkout/', views.checkout, name="checkout"),
    path('order-success/', views.order_success, name="order_success"),

    path('my-orders/', views.my_orders, name="my_orders"),

    # auth
    path('signup/', views.signup, name="signup"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
]
