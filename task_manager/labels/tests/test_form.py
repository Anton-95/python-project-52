from task_manager.labels.forms import LabelForm
from task_manager.labels.tests.test_case import LabelTestCase


class TestLabelForm(LabelTestCase):
    def test_valid_form(self):
        form = LabelForm(self.label_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        form = LabelForm({"name": ""})
        self.assertFalse(form.is_valid())
