from django.urls import path
from apps.users import views

urlpatterns = [path("", views.registration_page, name="registration")]
