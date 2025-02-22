from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
from task_manager.mixins import DeleteValidationMixin
from task_manager.views import LoginRequiredMixin


class LabelMixin:
    model = Label
    success_url = reverse_lazy("labels")


class LabelsView(LoginRequiredMixin, LabelMixin, ListView):
    template_name = "labels/labels_list.html"
    context_object_name = "labels"


class LabelCreateView(LoginRequiredMixin, LabelMixin, CreateView):
    form_class = LabelForm
    template_name = "labels/label_create.html"
    extra_context = dict(title="Создать метку", button="Создать")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно создана")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Метка с таким именем уже существует")
        return super().form_invalid(form)


class LabelUpdateView(LoginRequiredMixin, LabelMixin, UpdateView):
    form_class = LabelForm
    template_name = "labels/label_create.html"
    extra_context = dict(title="Изменение метки", button="Изменить")

    def form_valid(self, form):
        messages.success(self.request, "Метка успешно изменена")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Метка с таким именем уже существует")
        return super().form_invalid(form)


class LabelDeleteView(
    LoginRequiredMixin, DeleteValidationMixin, LabelMixin, DeleteView
):
    template_name = "delete_form.html"
    context_object_name = "model"
    extra_context = dict(title="метки")
    msg_success = "Метка успешно удалена"
    msg_error = "Невозможно удалить метку, потому что она используется"

    def is_protected(self):
        return self.object.tasks.exists()
