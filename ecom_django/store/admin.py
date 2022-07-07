from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer', 'quantity',
                    'price', 'address', 'phone']


admin.site.site_header = "Welcome To e-Shop"
admin.site.site_title = "e-Shop"
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
