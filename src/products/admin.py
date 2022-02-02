from django.contrib import admin
from .models import *


@admin.register(Table_Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'count', 'totality', 'price', 'price_device', 'price_per_quantity')


@admin.register(CartItem)
class CartitemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')


@admin.register(Table_Headers)
class Table_HeadersAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(ItemDevice)
class ItemDeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'product')
