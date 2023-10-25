from django.contrib import admin

from .models import *


@admin.register(BookGenre)
class BookGenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'author', 'image', 'genre')
    list_filter = ('name', 'price', 'author', 'genre')
    search_fields = ('name', 'price', 'author', 'genre')


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'generated_timestamp', 'user', 'book')
    list_filter = ('generated_timestamp', 'user')
    search_fields = ('quantity', 'generated_timestamp', 'user')
