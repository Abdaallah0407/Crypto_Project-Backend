from django.contrib import admin
from .models import *


@admin.register(BackCall)
class BackCallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'data_added')
    list_filter = ('name', 'phone',)
    list_display_links = ('name',)