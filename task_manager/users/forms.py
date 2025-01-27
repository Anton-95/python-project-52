from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from task_manager.users.models import User


class CustomUsersCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]


class CustomUsersUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password"]
