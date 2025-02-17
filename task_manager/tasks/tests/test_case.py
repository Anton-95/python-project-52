from django.test import Client, TestCase

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User


class TaskTestCase(TestCase):
    fixtures = [
        "test_tasks.json",
        "test_users.json",
        "test_statuses.json",
        "test_labels.json",
    ]

    def setUp(self):
        self.client = Client()
        self.task = Task.objects.get(pk=1)
        self.user = User.objects.get(pk=1)
        self.user_2 = User.objects.get(pk=2)
        self.label_1 = Label.objects.get(pk=1)
        self.label_2 = Label.objects.get(pk=2)
        self.status = Status.objects.get(pk=1)
        self.task_count = Task.objects.count()

        self.task_data = {
            "name": "New task",
            "description": "pu-pu-puuu",
            "status": self.status.id,
            "label": [self.label_1.id, self.label_2.id],
            "executor": self.user.id,
        }
