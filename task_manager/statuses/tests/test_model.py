from task_manager.statuses.models import Status
from task_manager.statuses.tests.test_case import StatusTestCase


class TestStatusModel(StatusTestCase):
    def test_status_create(self):
        Status.objects.create(name=self.status_data["name"])
        status = Status.objects.get(name=self.status_data["name"])
        self.assertEqual(status.name, self.status_data["name"])

    def test_status_dublicate(self):
        Status.objects.create(name=self.status_data["name"])
        with self.assertRaises(Exception):
            Status.objects.create(name="on break")
