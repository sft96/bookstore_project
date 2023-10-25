from django.contrib import admin

from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'email', 'is_active', 'date_joined', )
    list_filter = ('username',)
    search_fields = ('username', 'first_name', 'last_name')
