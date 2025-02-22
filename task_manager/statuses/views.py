from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import DeleteValidationMixin
from task_manager.statuses.forms import StatusForm
from task_manager.statuses.models import Status
from task_manager.views import LoginRequiredMixin


class BaseStatusMixin:
    model = Status
    success_url = reverse_lazy("statuses")


class StatusesView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/statuses_list.html"
    context_object_name = "statuses"


class StatusCreateView(LoginRequiredMixin, BaseStatusMixin, CreateView):
    form_class = StatusForm
    template_name = "statuses/status_create.html"
    extra_context = dict(title="Создать статус", button="Создать")

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Статус с таким именем уже существует.")
        return super().form_invalid(form)


class StatusUpdateView(LoginRequiredMixin, BaseStatusMixin, UpdateView):
    form_class = StatusForm
    template_name = "statuses/status_create.html"
    extra_context = dict(title="Изменить статус", button="Изменить")

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно изменен")
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteValidationMixin, DeleteView):
    model = Status
    template_name = "delete_form.html"
    context_object_name = "model"
    success_url = reverse_lazy("statuses")
    extra_context = dict(title="статуса")
    msg_success = "Статус успешно удален"
    msg_error = "Невозможно удалить статус, потому что он используется"
