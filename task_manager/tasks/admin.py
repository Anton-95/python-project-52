from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "author", "executor", "status", "created_at")
    search_fields = ["name"]
    list_filter = [("created_at", DateFieldListFilter)]
