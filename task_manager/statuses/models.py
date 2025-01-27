from django.db import models


class Status(models.Model):
    name = models.CharField("Имя", max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "statuses"
