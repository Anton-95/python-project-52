from django.test import Client, TestCase

from task_manager.statuses.models import Status
from task_manager.users.models import User


class StatusTestCase(TestCase):
    fixtures = ["test_statuses.json", "test_users.json"]

    def setUp(self):
        self.client = Client()
        self.status_count = Status.objects.count()
        self.status_1 = Status.objects.get(pk=1)
        self.status_2 = Status.objects.get(pk=2)
        self.user_1 = User.objects.get(pk=1)
        self.status_data = {"name": "on break"}
