from django.contrib.auth.forms import (AuthenticationForm,
                                       UserCreationForm,
                                       UserChangeForm)

from .models import CustomUser


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email',
                  'password1', 'password2']


class UserProfileForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'image', 'username', 'email')
