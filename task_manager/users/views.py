from webbrowser import get
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from task_manager.users.forms import UsersCreateForm
from task_manager.users.models import Users


class UsersView(ListView):
    model = Users
    template_name = "users/users.html"
    context_object_name = "users"


class UsersCreateView(CreateView):
    model = Users
    form_class = UsersCreateForm
    template_name = "users/users_create.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно создан")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Регистрация"
        context["button"] = "Зарегистрироваться"
        return context


class UsersUpdateView(UpdateView):
    model = Users
    form_class = UsersCreateForm
    template_name = "users/users_create.html"
    success_url = reverse_lazy("users")

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно обновлен")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменение пользователя"
        context["button"] = "Изменить"
        return context


class UsersDeleteView(DeleteView):
    model = Users
    template_name = "users/users_delete.html"
    success_url = reverse_lazy("users")
    context_object_name = "user"

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно удален")
        return super().form_valid(form)
