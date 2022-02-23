from django.contrib import admin

# Register your models here.
from .models import SaleItem, Sale


@admin.register(SaleItem)
class SaleItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale', 'data_added','product')
    list_filter = ('sale', 'product')
    list_display_links = ('sale', 'product')
    search_fields = ('product', 'sale', 'data_added')


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',
                    'data_added')
    list_filter = ('user',)
    list_display_links = ('user',)
    search_fields = ('user', 'id')
