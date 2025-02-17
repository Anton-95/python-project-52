from task_manager.tasks.forms import TaskCreateForm
from task_manager.tasks.tests.test_case import TaskTestCase


class TestTaskForm(TaskTestCase):
    def test_valid_form(self):
        form = TaskCreateForm(self.task_data)
        self.assertTrue(form.is_valid())

    def test_blank_form(self):
        task = self.task_data
        task["name"] = ""
        form = TaskCreateForm(task)
        self.assertFalse(form.is_valid())
