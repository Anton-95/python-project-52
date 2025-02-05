from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "date_joined")
    search_fields = ["username"]
    list_filter = [("date_joined", DateFieldListFilter)]
