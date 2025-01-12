"""
Модуль, в котором находятся модели с информацией о пользователях.
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    """
    Модель пользователя
    """

    Class = models.CharField(
        default="",
        max_length=64,
        help_text="Класс в котором учится ученик",
        verbose_name="Класс",
    )

    class Meta:
        db_table = "Users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["id"]
