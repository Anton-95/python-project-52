from django.contrib import messages
from django.forms import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.labels.forms import LabelForm
from task_manager.labels.models import Label
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


class LabelDeleteView(LoginRequiredMixin, LabelMixin, DeleteView):
    template_name = "delete_form.html"
    context_object_name = "model"
    extra_context = dict(title="метки")

    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, "Метка успешно удалена")
            return response
        except ValidationError:
            messages.error(
                request, "Невозможно удалить метку, потому что она используется"
            )
            return redirect("labels")
