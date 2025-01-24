from django import forms

from task_manager.users.models import Users


class UsersCreateForm(forms.ModelForm):
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Подтверждение пароля",
                "autocomplete": "new-password",
            }
        ),
        label="Подтверждение пароля",
    )

    class Meta:
        model = Users
        fields = ["first_name", "last_name", "username", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Имя пользователя",
                    "autofocus": "autofocus",
                }
            ),
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Фамилия"}
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Пароль",
                    "autocomplete": "new-password",
                }
            ),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if len(password) < 3:
            raise forms.ValidationError(
                        "Ваш пароль должен содержать как минимум 3 символа."
                    )

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают")

        return cleaned_data
