from task_manager.statuses.forms import StatusForm
from task_manager.statuses.tests.test_case import StatusTestCase


class TestStatusForm(StatusTestCase):
    def test_valid_form(self):
        form = StatusForm(self.status_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        form = StatusForm({"name": ""})
        self.assertFalse(form.is_valid())
