from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from task_manager.tasks.models import Task
from django.contrib import messages
from task_manager.statuses.views import CustomLoginRequiredMixin


class BaseTaskMixin:
    model = Task
    fields = ["name", "description", "status", "label", "executor"]
    success_url = reverse_lazy("tasks")


class TasksView(CustomLoginRequiredMixin, BaseTaskMixin, ListView):
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"


class TaskCreateView(CustomLoginRequiredMixin, BaseTaskMixin, CreateView):
    template_name = "tasks/tasks_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Создать задачу"
        context["button"] = "Создать"
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Задача успешно создана")
        return super().form_valid(form)


class TaskDetailView(CustomLoginRequiredMixin, BaseTaskMixin, DetailView):
    template_name = "tasks/task_detail.html"


class TaskUpdateView(CustomLoginRequiredMixin, BaseTaskMixin, UpdateView):
    template_name = "tasks/tasks_create.html"

    def form_valid(self, form):
        messages.success(self.request, "Задача успешно обновлена")
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Изменение задачи"
        context["button"] = "Изменить"
        return context


class TaskDeleteView(BaseTaskMixin, DeleteView):
    template_name = "tasks/task_delete.html"

    def dispatch(self, request, *args, **kwargs):
        task = self.get_object()
        if task.author != self.request.user:
            messages.error(request, "Вы можете удалять только свои задачи")
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, "Задача успешно удалена")
        return super().form_valid(form)
