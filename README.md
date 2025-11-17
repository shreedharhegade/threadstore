# 🛍️ ThreadStore – A Django E-Commerce Project

ThreadStore is a complete e-commerce website built with Django. It provides a full shopping experience, including user authentication, a session-based cart, product browsing, checkout, and order history.

This project demonstrates core Django concepts including models, views, templates, authentication, and session management.

## 🌟 Features

* **User Authentication:** Secure signup, login, and logout using Django's auth system.
* **Dynamic Homepage:** Displays all products, filterable by category.
* **Search & Filtering:**
  * Search for products by title.
  * Filter products by category.
* **Shopping Cart:** Session-based cart accessible only to logged-in users.
  * Add products with quantity.
  * Remove products from the cart.
  * View subtotals and total.
* **Secure Checkout:**
  * Collects user's name, email, and address.
  * Creates permanent `Order` and `OrderItem` records.
  * Clears cart after successful checkout.
* **Order Confirmation:** Displays a success page after ordering.
* **Order History:** Users can view all past orders with product details.
* **Responsive UI:** Built with Bootstrap 5 + Font Awesome.

---

## 🛠️ Technology Stack

* **Backend:** Django
* **Frontend:** HTML5, Bootstrap 5, Font Awesome
* **Database:** SQLite by default (supports PostgreSQL/MySQL)
* **Cart:** Django sessions

---

## 🚀 How to Run This Project

### 1. Clone the repository
```sh
git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git
cd YOUR-REPO
```

### 2. Create and activate virtual environment

**Windows**
```sh
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```sh
pip install django pillow
```

### 4. Configure media files

Add to `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

Add to project `urls.py`:
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your routes...
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 5. Apply migrations
```sh
python manage.py migrate
```

### 6. Create superuser
```sh
python manage.py createsuperuser
```

### 7. Run server
```sh
python manage.py runserver
```

Visit:  
http://127.0.0.1:8000/

---

## 🧩 Adding Products

1. Visit admin panel → http://127.0.0.1:8000/admin  
2. Log in using superuser  
3. Add categories  
4. Add products with images  

Products will now appear on the homepage.

---

## 📜 License

Licensed under the MIT License.
