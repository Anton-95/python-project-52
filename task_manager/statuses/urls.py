from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.StatusesView.as_view(), name='statuses'),
    path('create/', views.CreateStatusView.as_view(), name='status_create'),
    # path('<int:pk>/update/'),
    # path('<int:pk>/delete/')
]
