import django_filters
from django import forms

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskFilterForm(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        method="filter_my_tasks",
        label="Только свои задачи",
        widget=forms.CheckboxInput(attrs={"class": "form-check-input mr-3"}),
    )

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label="Статус",
        widget=forms.Select(attrs={"class": "form-select ml-2 mr-3"}),
    )

    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label="Исполнитель",
        widget=forms.Select(attrs={"class": "form-select ml-2 mr-3"}),
    )

    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        widget=forms.Select(attrs={"class": "form-select ml-2 mr-3"}),
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "label"]

    def filter_my_tasks(self, queryset, name, value):
        if value and self.request:
            return queryset.filter(author=self.request.user)
        return queryset


class TaskCreateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "executor", "label"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Имя"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Описание"}
            ),
            "status": forms.Select(attrs={"class": "form-select"}),
            "executor": forms.Select(attrs={"class": "form-select"}),
            "label": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "id": "id_labels"
                    }),
        }
