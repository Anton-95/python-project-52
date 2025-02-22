from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import DeleteValidationMixin
from task_manager.users.forms import (
    CustomUsersCreateForm,
    CustomUsersUpdateForm,
)
from task_manager.users.models import User
from task_manager.views import LoginRequiredMixin


class UserOwnersipCheckMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(
                request, "У вас нет прав для изменения другого пользователя."
            )
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class UsersView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"


class UsersCreateView(CreateView):
    model = User
    form_class = CustomUsersCreateForm
    template_name = "form.html"
    success_url = reverse_lazy("login")
    extra_context = dict(title="Регистрация", button="Зарегистрировать")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UsersUpdateView(LoginRequiredMixin, UserOwnersipCheckMixin, UpdateView):
    model = User
    form_class = CustomUsersUpdateForm
    template_name = "form.html"
    success_url = reverse_lazy("users")
    extra_context = dict(title="Изменение пользователя", button="Изменить")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UsersDeleteView(
    LoginRequiredMixin,
    DeleteValidationMixin,
    UserOwnersipCheckMixin,
    DeleteView
):
    model = User
    template_name = "delete_form.html"
    success_url = reverse_lazy("users")
    context_object_name = "model"
    extra_context = dict(title="пользователя")
    msg_success = "Пользователь успешно удален"
    msg_error = "Невозможно удалить пользователя, потому что он используется"
