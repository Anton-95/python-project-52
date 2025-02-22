from django.urls import reverse_lazy

from task_manager.tasks.models import Task
from task_manager.tasks.tests.test_case import TaskTestCase


class TestTaskView(TaskTestCase):
    def test_get_task_auth_user(self):
        user = self.user
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("tasks"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/tasks_list.html")

    def test_get_task_unauth_user(self):
        response = self.client.get(reverse_lazy("tasks"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_create_task_auth_user(self):
        user = self.user
        task_data = self.task_data
        task_count = self.task_count
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("task_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form.html")

        response = self.client.post(reverse_lazy("task_create"), task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("tasks"))
        self.assertEqual(Task.objects.count(), task_count + 1)

    def test_create_task_unauth_user(self):
        task_data = self.task_data
        task_count = self.task_count

        response = self.client.get(reverse_lazy("task_create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(reverse_lazy("task_create"), task_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertEqual(Task.objects.count(), task_count)

    def test_detail_task_auth_user(self):
        user = self.user
        task = self.task
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("task_detail", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tasks/task_detail.html")
        self.assertEqual(response.context["task"], task)

    def test_detail_task_unauth_user(self):
        task = self.task

        response = self.client.get(
            reverse_lazy("task_detail", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_update_task_auth_user(self):
        user = self.user
        task = self.task
        task_data = self.task_data
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("task_update", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form.html")

        response = self.client.post(
            reverse_lazy("task_update", kwargs={"pk": task.id}), task_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("tasks"))
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, task_data["name"])

    def test_update_task_unauth_user(self):
        task = self.task
        task_data = self.task_data

        response = self.client.get(
            reverse_lazy("task_update", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("task_update", kwargs={"pk": task.id}), task_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        updated_task = Task.objects.get(id=task.id)
        self.assertEqual(updated_task.name, task.name)

    def test_del_task_auth_user(self):
        user = self.user
        task = self.task
        task_count = self.task_count
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("task_delete", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete_form.html")

        response = self.client.post(
            reverse_lazy("task_delete", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("tasks"))
        self.assertEqual(Task.objects.count(), task_count - 1)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=task.id)

    def test_del_task_unauth_user(self):
        task = self.task
        task_count = self.task_count

        response = self.client.get(
            reverse_lazy("task_delete", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("task_delete", kwargs={"pk": task.id})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertEqual(Task.objects.count(), task_count)
