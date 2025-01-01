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
    model = SourceAnswers
    extra = 0
    min_num = 1


class PrototypeAnswerInline(admin.TabularInline):
    model = PrototypeAnswers
    extra = 0
    min_num = 1


class FormulaInline(admin.TabularInline):
    model = Formulas
    extra = 0
    min_num = 1


class LimitInline(admin.TabularInline):
    model = Limitations
    extra = 1


class TaskForm(forms.ModelForm):
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
