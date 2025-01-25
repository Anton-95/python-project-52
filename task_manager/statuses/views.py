from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, CreateView
from task_manager.statuses.models import Statuses
from task_manager.statuses.forms import StatusCreateForm


class StatusesView(ListView):
    model = Statuses
    template_name = 'statuses/statuses_list.html'
    content_object_name = 'statuses'


class CreateStatusView(CreateView):
    model = Statuses
    template_name = 'statuses/status_create.html'
    form_class = StatusCreateForm
    success_url = reverse_lazy('statuses')

    def form_valid(self, form):
        messages.success(self.request, "Статус успешно создан")
        return super().form_valid(form)
