from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Inline Order Items inside Order admin page
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # do not show empty rows


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "email", "created_at", "total_price")
    list_filter = ("created_at",)
    search_fields = ("name", "email", "user__username")
    inlines = [OrderItemInline]


class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "price", "stock")
    list_filter = ("category",)
    search_fields = ("title",)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)


