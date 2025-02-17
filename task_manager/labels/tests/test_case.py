from django.test import Client, TestCase

from task_manager.labels.models import Label
from task_manager.users.models import User


class LabelTestCase(TestCase):
    fixtures = ["test_labels.json", "test_users.json"]

    def setUp(self):
        self.client = Client()
        self.label_count = Label.objects.count()
        self.label = Label.objects.get(pk=1)
        self.user = User.objects.get(pk=1)
        self.label_data = {"name": "wontfix"}
