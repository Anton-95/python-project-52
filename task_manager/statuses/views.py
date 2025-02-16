from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.views import CustomLoginRequiredMixin


class BaseStatusMixin:
    model = Status
    success_url = reverse_lazy("statuses")


class StatusesView(CustomLoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"


class StatusCreateView(CustomLoginRequiredMixin, BaseStatusMixin, CreateView):
    form_class = StatusForm
    template_name = "statuses/status_create.html"

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Статус с таким именем уже существует.")
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать статус"
        context["button"] = "Создать"
        return context


class StatusUpdateView(CustomLoginRequiredMixin, BaseStatusMixin, UpdateView):
    form_class = StatusForm
    template_name = "statuses/status_create.html"

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно изменен")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменить статус"
        context["button"] = "Изменить"
        return context


class StatusDeleteView(CustomLoginRequiredMixin, DeleteView):
    model = Status
    template_name = "delete_form.html"
    context_object_name = "model"
    success_url = reverse_lazy("statuses")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "статуса"
        return context

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(self.request, "Статус успешно удален")
            return response
        except ProtectedError:
            messages.error(
                request, "Невозможно удалить статус, потому что он используется"
            )
            return redirect(self.success_url)
