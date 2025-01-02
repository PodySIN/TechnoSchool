"""
Модуль, который отвечает за формирование http маршрутов.
"""

from django.urls import path
from apps.main import views

urlpatterns = [path("", views.index_page, name="index")]
