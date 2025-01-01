from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from apps.main.service import get_base_context

from apps.task_upload.models import Questions, Topics

from apps.task_upload.forms import UploadTaskForm

from apps.task_upload.service import get_topics, get_source_tasks, task_upload


def task_upload_page(request: HttpRequest) -> HttpResponse:
    context = get_base_context("Task upload")
    context["UploadTask"] = UploadTaskForm()
    context["Questions"] = Questions.objects.all()
    context["Topics"] = get_topics()
    context["SourceTasks"] = get_source_tasks()
    if request.method == "POST":
        task_upload(request, UploadTaskForm(request.POST, request.FILES))
    return render(request, "pages/UploadTask.html", context)
