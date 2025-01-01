from django import forms

from apps.task_upload.models import SourceTasks


class UploadTaskForm(forms.Form):
    Image = forms.ImageField(
        label="Выберите изображение для задания (если нужно)",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    Video = forms.FileField(
        label="Выберите видео-решение (если нужно)",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    Solution = forms.ImageField(
        label="Выберите решение-изображение (если нужно)",
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
            }
        ),
    )
    Condition = forms.CharField(
        label="Условие задачи",
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Напишите условие задачи для последующей генерации, выделяя изменяемые числа так: @A@.",
                "class": "form-control",
                "style": "width:500px; height: 200px",
            }
        ),
    )
    Condition_for_students = forms.CharField(
        label="Условие задачи",
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Напишите условие задачи, которое будут видеть ученики",
                "class": "form-control",
                "style": "width:500px; height: 200px",
            }
        ),
    )
    Answer = forms.IntegerField(
        label="Ответ",
        required=True,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Ответ",
                "class": "form-control",
                "style": "width:400px; height: 30px",
            }
        ),
    )
