from django.db import models

from task_manager.statuses.models import Status
from task_manager.users.models import User


class Task(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=100, unique=True)
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Автор",
        related_name="tasks"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name="Статус",
        related_name="tasks"
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Исполнитель",
        related_name="task",
        blank=True,
        null=True
    )
    # label = models.ManyToManyField(
    #     "Label",
    #     verbose_name="Метки",
    #     related_name="tasks"
    # )
    created_at = models.DateTimeField(auto_now_add=True)
