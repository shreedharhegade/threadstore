from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product, Order, OrderItem, Category


def get_cart(request):
    return request.session.get("cart", {})


# HOME PAGE (with search + categories)
def home(request):
    query = request.GET.get("q", "")
    category_id = request.GET.get("cat", "")

    products = Product.objects.all()
    categories = Category.objects.all()

    if query:
        products = products.filter(title__icontains=query)

    if category_id:
        products = products.filter(category__id=category_id)

    return render(request, "store/home.html", {
        "products": products,
        "categories": categories,
        "query": query,
    })


# PRODUCT DETAIL
def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, "store/product_detail.html", {"product": product})


# CART
def add_to_cart(request, pk):
    # Check if user is logged in
    if not request.user.is_authenticated:
        return redirect("login")

    cart = get_cart(request)
    product = Product.objects.get(pk=pk)

    quantity = int(request.POST.get('quantity', 1))  # Get quantity from form, default to 1 if not provided

    # If the product already exists in the cart, increase the quantity
    if str(pk) in cart:
        cart[str(pk)] += quantity
    else:
        cart[str(pk)] = quantity

    request.session["cart"] = cart
    return redirect("cart")



def remove_from_cart(request, pk):
    if not request.user.is_authenticated:
        return redirect("login")

    cart = get_cart(request)
    cart.pop(str(pk), None)
    request.session["cart"] = cart
    return redirect("cart")


def cart_view(request):
    # 🔒 User must be logged in
    if not request.user.is_authenticated:
        return redirect("login")

    cart = get_cart(request)
    items = []
    total = 0

    for product_id, qty in cart.items():
        product = Product.objects.get(pk=product_id)
        items.append({"product": product, "qty": qty, "subtotal": product.price * qty})
        total += product.price * qty

    return render(request, "store/cart.html", {"items": items, "total": total})


# CHECKOUT
def checkout(request):
    # 🔒 User must be logged in to place an order
    if not request.user.is_authenticated:
        return redirect("login")

    cart = get_cart(request)

    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]

        # ✅ Always link order to logged-in user
        order = Order.objects.create(
            user=request.user,
            name=name,
            email=email,
            address=address,
        )

        for product_id, qty in cart.items():
            product = Product.objects.get(pk=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                price=product.price,
            )

        request.session["cart"] = {}  # clear cart
        return redirect("order_success")

    return render(request, "store/checkout.html")


def order_success(request):
    return render(request, "store/order_success.html")


# MY ORDERS (list orders + items)
def my_orders(request):
    if not request.user.is_authenticated:
        return redirect("login")

    # prefetch items and products for performance
    orders = (
        Order.objects
        .filter(user=request.user)
        .prefetch_related("orderitem_set__product")
        .order_by("-created_at")
    )

    return render(request, "store/my_orders.html", {"orders": orders})


# AUTH
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "store/signup.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "store/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("home")
