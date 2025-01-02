"""
Модуль, который отвечает за взаимодействие с пользователями сайта.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apps.main.configure import configure_logging

logger = configure_logging()


def registration_page(request: HttpRequest) -> HttpResponse:
    """
    Отображает страницу регистрации.
    """
    logger.info("пользователь перешел на страницу регистрации")
    return render(request, "pages/registration.html")
