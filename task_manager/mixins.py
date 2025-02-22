from django.contrib import messages
from django.db.models.deletion import ProtectedError
from django.forms import ValidationError
from django.shortcuts import redirect


class DeleteValidationMixin:
    def post(self, request, *args, **kwargs):
        try:
            response = super().post(request, *args, **kwargs)
            messages.success(request, self.msg_success)
            return response
        except ProtectedError:
            messages.error(request, self.msg_error)
            return redirect(self.success_url)
        except ValidationError:
            messages.error(request, self.msg_error)
            return redirect(self.success_url)
