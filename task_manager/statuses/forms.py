from django import forms
from task_manager.statuses.models import Status


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ["name"]
