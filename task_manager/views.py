from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm as AuthForm
from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequired
from django.contrib.auth.views import LoginView as UserLoginView
from django.contrib.auth.views import LogoutView as UserLogoutView
from django.shortcuts import redirect
from django.urls import reverse_lazy


class LoginRequiredMixin(LoginRequired):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(
                request, ("Вы не авторизованы! Пожалуйста, выполните вход.")
                )
            return redirect(reverse_lazy("login"))
        return super().dispatch(request, *args, **kwargs)


class LoginView(UserLoginView):
    template_name = "login.html"
    form_class = AuthForm

    def form_valid(self, form):
        messages.success(self.request, "Вы залогинены")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(
            self.request,
            """Пожалуйста, введите правильные имя пользователя и пароль.
            Оба поля могут быть чувствительны к регистру.""",
        )
        return super().form_invalid(form)


class LogoutView(UserLogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.info(request, "Вы разлогинены")
        return super().dispatch(request, *args, **kwargs)
