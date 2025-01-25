from django import forms
from task_manager.statuses.models import Statuses


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["name"]
