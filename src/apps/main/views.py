"""
Модуль, который отвечает за основную логику, а также idex page.
"""

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from apps.main.configure import configure_logging

logger = configure_logging()


def index_page(request: HttpRequest) -> HttpResponse:
    """
    Отображение главной страницы на сайте
    """
    logger.info("Пользователь перешел на главную страницу")
    return render(request, "pages/index.html")
