from django.urls import reverse_lazy

from task_manager.labels.models import Label
from task_manager.labels.tests.test_case import LabelTestCase


class TestLabelViews(LabelTestCase):
    def test_get_labels_auth_user(self):
        user = self.user
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("labels"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.label_count, Label.objects.count())
        self.assertTemplateUsed(response, "labels/labels_list.html")

    def test_get_labels_unauth_user(self):
        response = self.client.get(reverse_lazy("labels"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_label_create_auth_user(self):
        user = self.user
        label_count = self.label_count
        self.client.force_login(user)

        response = self.client.get(reverse_lazy("label_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels/label_create.html")

        response = self.client.post(
            reverse_lazy("label_create"), self.label_data
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("labels"))
        self.assertEqual(Label.objects.count(), label_count + 1)

    def test_label_create_unauth_user(self):
        response = self.client.get(reverse_lazy("label_create"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("label_create"), self.label_data
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_label_update_auth_user(self):
        user = self.user
        label = self.label
        update_label_data = self.label_data
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("label_update", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "labels/label_create.html")

        response = self.client.post(
            reverse_lazy("label_update", kwargs={"pk": label.id}),
            update_label_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("labels"))
        updated_label = Label.objects.get(id=label.id)
        self.assertEqual(updated_label.name, update_label_data["name"])

    def test_label_update_unauth_user(self):
        label = self.label

        response = self.client.get(
            reverse_lazy("label_update", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("label_update", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_label_del_auth_user(self):
        user = self.user
        label = self.label
        label_count = self.label_count
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("label_delete", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete_form.html")

        response = self.client.post(
            reverse_lazy("label_delete", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("labels"))
        self.assertEqual(Label.objects.count(), label_count - 1)
        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(id=label.id)

    def test_label_del_unauth_user(self):
        label = self.label
        label_count = self.label_count

        response = self.client.get(
            reverse_lazy("label_delete", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

        response = self.client.post(
            reverse_lazy("label_delete", kwargs={"pk": label.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))
        self.assertEqual(Label.objects.count(), label_count)
