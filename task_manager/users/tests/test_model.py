from task_manager.users.models import User
from task_manager.users.tests.test_case import UserTestCase


class TestUserModel(UserTestCase):
    def test_user_create(self):
        User.objects.create(
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            username=self.user_data["username"],
            password=self.user_data["password1"],
        )

        user = User.objects.get(username=self.user_data["username"])

        self.assertEqual(user.username, self.user_data["username"])
        self.assertEqual(user.first_name, self.user_data["first_name"])
        self.assertEqual(user.last_name, self.user_data["last_name"])
        self.assertEqual(
            str(user),
            f'{self.user_data["first_name"]} {self.user_data["last_name"]}',
        )

    def test_dublicate_username(self):
        User.objects.create(
            first_name=self.user_data["first_name"],
            last_name=self.user_data["last_name"],
            username=self.user_data["username"],
            password=self.user_data["password1"],
        )

        with self.assertRaises(Exception):
            User.objects.create(
                first_name="Maxim",
                last_name="Smirnov",
                username="Incognito",
                password="qwerty",
            )
