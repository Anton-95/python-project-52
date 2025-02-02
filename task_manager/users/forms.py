from django import forms
from django.contrib.auth.forms import UserCreationForm

from task_manager.users.models import User


class CustomUsersCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2"
            ]


class CustomUsersUpdateForm(CustomUsersCreateForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            if self.user and self.user.username != username:
                raise forms.ValidationError(
                    "Пользователь с таким именем уже существует"
                    )
        return username
