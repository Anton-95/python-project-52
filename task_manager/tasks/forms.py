import django_filters
from django import forms

from task_manager.labels.models import Label
from task_manager.tasks.models import Task


class TaskFilterForm(django_filters.FilterSet):
    self_tasks = django_filters.BooleanFilter(
        method="filter_my_tasks",
        label="Только свои задачи",
        widget=forms.CheckboxInput(),
    )

    label = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label="Метка",
        widget=forms.Select(),
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "label"]

    def filter_my_tasks(self, queryset, name, value):
        if value and self.request:
            return queryset.filter(author=self.request.user)
        return queryset
