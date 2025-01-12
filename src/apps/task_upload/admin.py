"""
Модуль, который отвечает за админ панель(Банк заданий).
"""

from django.contrib import admin
from apps.task_upload.models import (
    Questions,
    Topics,
    PrototypeTasks,
    SourceTasks,
    Formulas,
    StartVariablesLimitations,
    SourceAnswers,
    PrototypeAnswers,
)
from apps.task_upload.admin_service import (
    SourceAnswerInline,
    FormulaInline,
    TaskForm,
    PrototypeAnswerInline,
    generate_similar_tasks,
    FollowingLimitationsInline,
    StartLimitationsInline,
    VariablesInline,
)


class SourceTasksAdmin(admin.ModelAdmin):
    """
    Кастомизация вкладки с шаблонами в админ панели.
    """

    list_display = ("id", "Number", "Topic", "Condition_for_students", "time_create", "time_update")
    list_display_links = ("id",)
    search_fields = ("id", "Condition_for_students")
    list_filter = ("Number", "Topic")
    inlines = (
        SourceAnswerInline,
        VariablesInline,
        StartLimitationsInline,
        FormulaInline,
        FollowingLimitationsInline,
    )
    fields = (
        "Number",
        "Topic",
        "Image",
        "Condition_for_students",
        "Condition",
        "Solution",
        "Video",
    )
    actions = [generate_similar_tasks]
    readonly_fields = ["time_create", "time_update"]
    empty_value_display = "-ничего-"
    list_per_page = 12
    form = TaskForm
    generate_similar_tasks.short_description = "Сгенерировать похожие задания"

    class Media:
        css = {"all": ("css/admin.css",)}


class PrototypeTasksAdmin(admin.ModelAdmin):
    """
    Кастомизация вкладки с прототипами в админ панели.
    """

    list_display = ("id", "Number", "Topic", "Condition", "time_create", "time_update")
    list_display_links = ("id",)
    search_fields = ("id", "Condition")
    list_filter = ("Number", "Topic", 'SourceTask_id')
    inlines = [PrototypeAnswerInline]
    fields = (
        "Number",
        "Topic",
        "Image",
        "Condition",
        "SourceTask",
    )
    readonly_fields = ["time_create", "time_update"]
    empty_value_display = "-ничего-"
    list_per_page = 12
    form = TaskForm

    class Media:
        css = {"all": ("css/admin.css",)}


class TopicsTasksAdmin(admin.ModelAdmin):
    """
    Кастомизация вкладки с темами в админ панели.
    """

    list_per_page = 20
    search_fields = (
        "id",
        "Topic",
    )
    list_filter = ("question_id",)


"""
Регистрация баз данных в админ панели.
"""
admin.site.register(Questions)
admin.site.register(Topics, TopicsTasksAdmin)
admin.site.register(SourceTasks, SourceTasksAdmin)
admin.site.register(PrototypeTasks, PrototypeTasksAdmin)
