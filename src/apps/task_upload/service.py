from apps.main.service import get_all_objects_from_model, get_objects_from_model_by_filter

from apps.task_upload.models import Formulas, Limitations, Topics, SourceTasks, PrototypeTasks
from django.shortcuts import redirect


def task_upload(request, form):
    if form.is_valid():
        number = request.POST["TaskNumber"]
        topic = request.POST["TopicName"]
        condition_for_students = form.data.get("Condition_for_students")
        answer = form.data.get("Answer")
        is_prototype = request.POST["IsSource"]
        if is_prototype == "Да":
            next_task_id = list(get_all_objects_from_model(PrototypeTasks))[-1].id + 1
            source_task_id = int(request.POST["WhatTask"])
            task = PrototypeTasks.objects.create(
                Number=number,
                Condition=condition_for_students,
                Topic=topic,
                Answer=answer,
                SourceTask_id=source_task_id,
            )
            if "Image" in request.FILES:
                image = request.FILES["Image"]
                exp = image.name.split(".")[1]
                image.name = f"{number}_{next_task_id}.{exp}"
                task.Image = image
            task.save()
        else:
            next_task_id = list(get_all_objects_from_model(SourceTasks))[-1].id + 1
            condition = form.data.get("Condition")
            task = SourceTasks.objects.create(
                Number=number,
                Condition=condition,
                Topic=topic,
                Answer=answer,
                Condition_for_students=condition_for_students,
            )

            if "Image" in request.FILES:
                image = request.FILES["Image"]
                exp = image.name.split(".")[1]
                image.name = f"{number}_{next_task_id}.{exp}"
                task.Image = image
            if "Video" in request.FILES:
                video = request.FILES["Video"]
                exp = video.name.split(".")[1]
                video.name = f"{number}_{next_task_id}.{exp}"
                task.Video = video
            if "Solution" in request.FILES:
                solution = request.FILES["Solution"]
                exp = solution.name.split(".")[1]
                solution.name = f"{number}_{next_task_id}.{exp}"
                task.Solution = solution
            limits = [val for key, val in request.POST.items() if key.startswith("Limitation")]
            formuls = [val for key, val in request.POST.items() if key.startswith("Formula")]
            for limit in limits:
                new_limit = Limitations.objects.create(Limitation=limit, Task_id=next_task_id)
                new_limit.save()
            for formula in formuls:
                new_formula = Formulas.objects.create(Formula=formula, Task_id=next_task_id)
                new_formula.save()
            task.save()
    return redirect("TaskUpload/")


def get_topics():
    topics = Topics.objects.all()
    topics_dict = {}
    for topic in topics:
        key = str(topic.question_id)
        value = topic.Topic
        if key not in topics_dict:
            topics_dict[key] = [value]
        else:
            topics_dict[key].append(value)
    return topics_dict


def get_source_tasks():
    source_tasks = SourceTasks.objects.all()
    source_tasks_dict = {}
    for source_task in source_tasks:
        key = str(source_task.Number)
        value = source_task.id
        value2 = source_task.Topic
        if key not in source_tasks_dict:
            source_tasks_dict[key] = [[value, value2]]
        else:
            source_tasks_dict[key].append([value, value2])
    return source_tasks_dict
