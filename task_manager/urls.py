from django.contrib import admin
from django.urls import include, path
from task_manager import views
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("users/", include("task_manager.users.urls")),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
