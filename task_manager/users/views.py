from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import redirect

from task_manager.users.forms import CustomUsersCreateForm, CustomUsersUpdateForm
from task_manager.users.models import Users


class UsersView(ListView):
    model = Users
    template_name = "users/users.html"
    context_object_name = "users"


class UsersCreateView(CreateView):
    model = Users
    form_class = CustomUsersCreateForm
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
    form_class = CustomUsersUpdateForm
    template_name = "users/users_create.html"
    success_url = reverse_lazy("users")

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(request, "Вы можете изменять только свой профиль.")
            return redirect("users")
        return super().dispatch(request=request, *args, **kwargs)

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

    def dispatch(self, request, *args, **kwargs):
        if self.get_object() != self.request.user:
            messages.error(request, "Вы можете удалять только свой профиль.")
            return redirect("users")
        return super().dispatch(request=request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Пользователь успешно удален")
        return super().form_valid(form)
