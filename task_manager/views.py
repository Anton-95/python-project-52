from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView


class CustomLoginView(LoginView):
    template_name = "login.html"
    form_class = AuthenticationForm

    def form_valid(self, form):
        messages.success(self.request, "Вы успешно вошли в систему")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request, "Неправильное имя пользователя или пароль."
        )
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы успешно вышли из системы")
        return super().dispatch(request, *args, **kwargs)
