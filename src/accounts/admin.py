from django.contrib import admin
from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',
                    'phone_number')
    list_filter = ('is_staff', 'username', 'email')
    list_display_links = ('username',)
    list_editable = ('is_staff',)
