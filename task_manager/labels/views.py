from django.urls import reverse_lazy
from django.views.generic import ListView
from task_manager.labels.models import Label


class LabelMixin:
    model = Label
    fields = ["name"]
    success_url = reverse_lazy("labels")


class LabelsView(LabelMixin, ListView):
    template_name = "labels/labels_list.html"
