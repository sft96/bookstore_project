from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='books:index'),
         name='logout')
]
