from django.contrib import messages
from django.contrib.auth.views import LoginView
# from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = "login.html"
    # form_class = AuthenticationForm

    def form_valid(self, form):
        print(self.request.POST)
        messages.success(self.request, "Вы успешно вошли в систему")
        return super().form_valid(form)
