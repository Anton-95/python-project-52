from django.test import Client, TestCase

from task_manager.labels.models import Label
from task_manager.users.models import User


class LabelTestCase(TestCase):
    fixtures = ["test_labels.json", "test_users.json"]

    def setUp(self):
        self.client = Client()
        self.label_count = Label.objects.count()
        self.label_1 = Label.objects.get(pk=1)
        self.label_2 = Label.objects.get(pk=2)
        self.user_1 = User.objects.get(pk=1)
        self.user_2 = User.objects.get(pk=2)
        self.label_data = {"name": "wontfix"}
