"""
Модуль, в котором находятся вспомогательные функции для работы с админ панелью.
"""

from django.contrib import admin
from apps.task_upload.models import (
    Questions,
    Topics,
    PrototypeTasks,
    SourceTasks,
    Formulas,
    Limitations,
    SourceAnswers,
    PrototypeAnswers,
)
from django import forms


class SourceAnswerInline(admin.TabularInline):
    """
    Класс, который создает поле для добавления дополнительных ответов для шаблонов.
    """

    model = SourceAnswers
    extra = 1


class PrototypeAnswerInline(admin.TabularInline):
    """
    Класс, который создает поле для добавления дополнительных ответов для прототипов.
    """

    model = PrototypeAnswers
    extra = 1


class FormulaInline(admin.TabularInline):
    """
    Класс, который создает поле для добавления дополнительных шагов решения.
    """

    model = Formulas
    extra = 1


class LimitInline(admin.TabularInline):
    """
    Класс, который создает поле для добавления дополнительных ограничений.
    """

    model = Limitations
    extra = 1


class TaskForm(forms.ModelForm):
    """
    Класс, который переопределяет стандартную форму в админ панели.
    """

    class Meta:
        model = SourceTasks
        fields = "__all__"  # Или перечислите поля вручную
        widgets = {
            "Condition": forms.Textarea(
                attrs={
                    "cols": 80,  # Ширина поля
                    "rows": 10,  # Высота поля
                    "style": "resize: both;",  # Разрешаем изменять размер
                }
            ),
            "Condition_for_students": forms.Textarea(
                attrs={
                    "cols": 80,  # Ширина поля
                    "rows": 10,  # Высота поля
                    "style": "resize: both;",  # Разрешаем изменять размер
                }
            ),
        }


def generate_similar_tasks():
    """
    Генерирует задания, на основе шаблона.
    """
    pass
