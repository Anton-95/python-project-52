from django.db import models
from django.forms import ValidationError


class Label(models.Model):
    name = models.CharField("Имя", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        if self.tasks.exists():
            raise ValidationError("Нельзя удалить метку связанную с задачей")
        super().delete(*args, **kwargs)

    class Meta:
        db_table = "labels"
