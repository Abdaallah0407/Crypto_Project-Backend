from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *

# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'createdAt', 'get_image')
    list_display_links = ['title']
    list_filter = ('title', 'description')
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="40" height="60">')

    get_image.short_description = "Миниатюра"