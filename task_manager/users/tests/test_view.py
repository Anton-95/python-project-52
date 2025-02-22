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
        self.assertTemplateUsed("form.html")

        response = self.client.post(reverse_lazy("users_create"), user_data)
        self.assertEqual(User.objects.count(), user_count + 1)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_del_unauth_user(self):
        response = self.client.get(
            reverse_lazy("users_delete", kwargs={"pk": 1})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_del_auth_user(self):
        user = self.user_1
        self.client.force_login(user)
        users_count = User.objects.count()

        response = self.client.get(
            reverse_lazy("users_delete", kwargs={"pk": user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "delete_form.html")

        response = self.client.post(
            reverse_lazy("users_delete", kwargs={"pk": user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))
        self.assertEqual(User.objects.count(), users_count - 1)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(id=user.id)

    def test_update_unauth_user(self):
        response = self.client.get(
            reverse_lazy("users_update", kwargs={"pk": 1})
            )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("login"))

    def test_update_auth_user(self):
        user = self.user_1
        update_user_data = self.user_data
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("users_update", kwargs={"pk": user.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "form.html")

        response = self.client.post(
            reverse_lazy("users_update", kwargs={"pk": user.id}),
            update_user_data
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))
        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.username, "Incognito")
        self.assertEqual(updated_user.first_name, "John")
        self.assertEqual(updated_user.last_name, "Doe")

    def test_update_another_user(self):
        user = self.user_1
        another_user = self.user_2
        self.client.force_login(user)

        response = self.client.get(
            reverse_lazy("users_update", kwargs={"pk": another_user.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy("users"))
