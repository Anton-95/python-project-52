from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    class Meta:
        db_table = "users"
