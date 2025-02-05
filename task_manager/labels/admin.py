from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import Label


@admin.register(Label)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ["name"]
    list_filter = [("created_at", DateFieldListFilter)]
