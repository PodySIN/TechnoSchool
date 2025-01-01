from django.urls import path
from apps.task_upload import views

urlpatterns = [
    path("", views.task_upload_page, name="upload_task"),
]
