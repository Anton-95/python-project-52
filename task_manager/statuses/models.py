from django.db import models


class Statuses(models.Model):
    name = models.CharField('Имя', max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.task_set.all().count() != 0:
            raise Exception('Нельзя удалять статус с задачами')
        super().delete(*args, **kwargs)

    class Meta:
        db_table = "statuses"
