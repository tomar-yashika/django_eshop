from django.contrib import admin
from .models.Product import Product
from .models.Category import Category
from .models.Customer import Customer
from .models.Price_filter import Filter_Price


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'contact']


# Register your models here.


admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Filter_Price)