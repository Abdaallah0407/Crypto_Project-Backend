from django.contrib import admin
from .models import *


@admin.register(Table_Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', 'totality', 'price', 'price_device')


@admin.register(CartItem)
class CartitemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')


@admin.register(Table_Headers)
class Table_HeadersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
