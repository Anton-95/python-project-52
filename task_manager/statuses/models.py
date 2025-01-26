from django.core.exceptions import ValidationError
from django.db import models


class Statuses(models.Model):
    name = models.CharField("Имя", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    # def delete(self, *args, **kwargs):
    #     if self.task_set.exists():
    #         raise ValidationError(
    #             "Невозможно удалить статус, так как с ним связаны задачи."
    #         )
    #     super().delete(*args, **kwargs)

    class Meta:
        db_table = "statuses"
