from django.test import Client, TestCase

from task_manager.users.models import User


class UserTestCase(TestCase):
    fixtures = ["test_users.json"]

    def setUp(self):
        self.client = Client()
        self.user_count = User.objects.count()
        self.user_1 = User.objects.get(pk=1)
        self.user_2 = User.objects.get(pk=2)

        self.user_data = {
            "first_name": "John",
            "last_name": "Doe",
            "username": "Incognito",
            "password1": "123",
            "password2": "123",
        }
