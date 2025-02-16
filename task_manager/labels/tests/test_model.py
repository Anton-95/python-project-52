from task_manager.labels.models import Label
from task_manager.labels.tests.test_case import LabelTestCase


class TestLabelModel(LabelTestCase):
    def test_label_create(self):
        Label.objects.create(name=self.label_data["name"])
        label = Label.objects.get(name=self.label_data["name"])
        self.assertEqual(label.name, self.label_data["name"])

    def test_label_dublicate(self):
        Label.objects.create(name=self.label_data["name"])
        with self.assertRaises(Exception):
            Label.objects.create(name="wontfix")
