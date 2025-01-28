from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from task_manager.tasks.models import Task
from django.contrib import messages


class TasksView(ListView):
    model = Task
    template_name = "tasks/tasks_list.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    template_name = "tasks/tasks_create.html"
    fields = ['name', 'description', 'status', 'executor']
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Задача успешно создана")
        return super().form_valid(form)
