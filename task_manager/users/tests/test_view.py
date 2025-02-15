from django.urls import reverse_lazy

from task_manager.users.models import User
from task_manager.users.tests.test_case import UserTestCase


class TestUserViews(UserTestCase):
    def test_get_users(self):
        response = self.client.get(reverse_lazy("users"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user_count, User.objects.count())
        self.assertTemplateUsed(response, "users/users_list.html")

    def test_create_user(self):
        user_data = self.user_data
        user_count = self.user_count

        response = self.client.get(reverse_lazy("users_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("users/users_create.html")

        response = self.client.post(reverse_lazy("users_create"), user_data)
        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_del_unauthorized_user(self):
        response = self.client.get(
            reverse_lazy("users_delete", kwargs={"pk": 1})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_del_authorized_user(self):
        user_1 = self.user_1
        self.client.force_login(user_1)
        users_count = User.objects.count()

        response = self.client.get(
            reverse_lazy("users_delete", kwargs={"pk": user_1.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete_form.html")

        response = self.client.post(
            reverse_lazy("users_delete", kwargs={"pk": user_1.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))
        self.assertEqual(User.objects.count(), users_count - 1)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user_1.id)
