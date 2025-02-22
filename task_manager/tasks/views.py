from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.tasks.forms import TaskCreateForm, TaskFilterForm
from task_manager.tasks.models import Task
from task_manager.views import LoginRequiredMixin


class BaseTaskMixin:
    model = Task
    success_url = reverse_lazy("tasks")


class TasksView(LoginRequiredMixin, BaseTaskMixin, FilterView):
    filterset_class = TaskFilterForm
    template_name = "tasks/tasks_list.html"


class TaskCreateView(LoginRequiredMixin, BaseTaskMixin, CreateView):
    template_name = "tasks/tasks_create.html"
    form_class = TaskCreateForm
    extra_context = dict(title="Создать задачу", button="Создать")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Задача успешно создана")
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, BaseTaskMixin, DetailView):
    template_name = "tasks/task_detail.html"


class TaskUpdateView(LoginRequiredMixin, BaseTaskMixin, UpdateView):
    template_name = "tasks/tasks_create.html"
    form_class = TaskCreateForm
    extra_context = dict(title="Изменение задачи", button="Изменить")

    def form_valid(self, form):
        messages.success(self.request, "Задача успешно изменена")
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, BaseTaskMixin, DeleteView):
    template_name = "delete_form.html"
    context_object_name = "model"
    extra_context = dict(title="задачи")

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        task = self.get_object()
        if task.author != self.request.user:
            messages.error(request, "Задачу может удалить только ее автор.")
            return redirect(self.success_url)
        return response

    def form_valid(self, form):
        messages.success(self.request, "Задача успешно удалена")
        return super().form_valid(form)
