from task_manager.tasks.models import Task
from task_manager.tasks.tests.test_case import TaskTestCase


class TestTaskModel(TaskTestCase):
    def test_task_create(self):
        task = Task.objects.create(
            name=self.task_data["name"],
            description=self.task_data["description"],
            status=self.status,
            executor=self.user,
            author=self.user_2,
        )
        task.label.set([self.label_1, self.label_2])
        self.assertEqual(task.name, self.task_data["name"])
        self.assertEqual(task.description, self.task_data["description"])
        self.assertEqual(task.status, self.status)
        self.assertEqual(task.executor, self.user)
        self.assertEqual(task.author, self.user_2)
        self.assertCountEqual(
            list(task.label.all()), [self.label_1, self.label_2]
            )
