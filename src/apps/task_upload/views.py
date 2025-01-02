"""
Модуль, который отвечает за добавление новых заданий
"""

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from apps.main.service import get_base_context
