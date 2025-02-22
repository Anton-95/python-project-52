from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.users.forms import (
    CustomUsersCreateForm,
    CustomUsersUpdateForm,
)
from task_manager.users.models import User
from task_manager.views import LoginRequiredMixin


class UsersView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"


class UsersCreateView(CreateView):
    model = User
    form_class = CustomUsersCreateForm
    template_name = "users/users_create.html"
    success_url = reverse_lazy("login")
    extra_context = dict(title="Регистрация", button="Зарегистрировать")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно зарегистрирован")
        return super().form_valid(form)


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = CustomUsersUpdateForm
    template_name = "users/users_create.html"
    success_url = reverse_lazy("users")
    extra_context = dict(title="Изменение пользователя", button="Изменить")

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated and \
            self.get_object() != self.request.user:
            messages.error(
                request, "У вас нет прав для изменения другого пользователя."
            )
            return redirect(self.success_url)
        return response

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, "Пользователь успешно изменен")
            return response
        except ValidationError:
            messages.error(
                request, "Пользователь с таким именем уже существует"
                )
            return redirect(self.success_url)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class UsersDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "delete_form.html"
    success_url = reverse_lazy("users")
    context_object_name = "model"
    extra_context = dict(title="пользователя")

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, "Пользователь успешно удален")
            return response
        except ProtectedError:
            messages.error(
                request,
                "Невозможно удалить пользователя, потому что он используется"
            )
            return redirect(self.success_url)

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        if request.user.is_authenticated and \
            self.get_object() != self.request.user:
            messages.error(
                request,
                "У вас нет прав для изменения другого пользователя."
                )
            return redirect(self.success_url)
        return response
