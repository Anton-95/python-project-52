from django.urls import reverse_lazy

from task_manager.statuses.models import Status
from task_manager.statuses.tests.test_case import StatusTestCase


class TestStatusView(StatusTestCase):
    def test_get_statuses_auth_user(self):
        user = self.user
        status_count = self.status_count
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("statuses"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/statuses_list.html")
        self.assertEqual(Status.objects.count(), status_count)

    def test_get_statuses_unauth_user(self):
        response = self.client.get(reverse_lazy("statuses"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_create_status_auth_user(self):
        user = self.user
        status_data = self.status_data
        status_count = self.status_count
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("status_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/status_create.html")

        response = self.client.post(reverse_lazy("status_create"), status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("statuses"))
        self.assertEqual(Status.objects.count(), status_count + 1)

    def test_create_status_unauth_user(self):
        status_data = self.status_data

        response = self.client.get(reverse_lazy("status_create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(reverse_lazy("status_create"), status_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_update_status_auth_user(self):
        user = self.user
        status = self.status
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("status_update", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/status_create.html")

        response = self.client.post(
            reverse_lazy("status_update", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "statuses/status_create.html")

    def test_update_status_unauth_user(self):
        status = self.status

        response = self.client.get(
            reverse_lazy("status_update", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("status_update", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_del_status_auth_user(self):
        user = self.user
        status = self.status
        status_count = self.status_count
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("status_delete", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete_form.html")

        response = self.client.post(
            reverse_lazy("status_delete", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("statuses"))
        self.assertEqual(Status.objects.count(), status_count - 1)
        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(id=status.id)

    def test_del_status_unauth_user(self):
        status = self.status
        status_count = self.status_count

        response = self.client.get(
            reverse_lazy("status_delete", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("status_delete", kwargs={"pk": status.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertEqual(Status.objects.count(), status_count)
