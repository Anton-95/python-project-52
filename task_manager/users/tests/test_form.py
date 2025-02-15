from task_manager.users.forms import CustomUsersCreateForm
from task_manager.users.tests.test_case import UserTestCase


class TestUserForm(UserTestCase):
    def test_valid_form(self):
        form = CustomUsersCreateForm(self.user_data)
        self.assertTrue(form.is_valid())

    def test_blank_fields(self):
        form = CustomUsersCreateForm({"username": "Test", "password1": "123"})
        self.assertFalse(form.is_valid())

    def test_invalid_username(self):
        user_data = self.user_data
        user_data["username"] = "$#%"
        form = CustomUsersCreateForm(user_data)
        self.assertFalse(form.is_valid())

    def test_password_lenghth(self):
        user_data = self.user_data
        user_data["password1"] = "12"
        form = CustomUsersCreateForm(user_data)
        self.assertFalse(form.is_valid())

    def test_password_matching(self):
        user_data = self.user_data
        user_data["password1"], user_data["password2"] = "1234", "12345"
        form = CustomUsersCreateForm(user_data)
        self.assertFalse(form.is_valid())
