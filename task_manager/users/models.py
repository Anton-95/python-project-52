from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
