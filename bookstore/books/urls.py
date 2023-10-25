from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/add/<int:book_id>/', views.basket_add, name='basket_add'),
    path('book/remove/<int:basket_id>/', views.basket_remove,
         name='basket_remove'),
    path('book/<int:pk>/', views.book, name='book'),
    path('genre/<int:pk>/', views.genre, name='genre'),
]
