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
from apps.task_upload.admin_service import (
    SourceAnswerInline,
    FormulaInline,
    LimitInline,
    TaskForm,
    PrototypeAnswerInline,
)


def generate_similar_tasks():
    pass


class SourceTasksAdmin(admin.ModelAdmin):
    list_display = ("id", "Number", "Topic", "Condition_for_students", "time_create", "time_update")
    list_display_links = ("id",)
    search_fields = ("id", "Condition_for_students")
    list_filter = ("Number", "Topic")
    inlines = [SourceAnswerInline, FormulaInline, LimitInline]
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
    generate_similar_tasks.description = "Сгенерировать "


class PrototypeTasksAdmin(admin.ModelAdmin):
    list_display = ("id", "Number", "Topic", "Condition", "time_create", "time_update")
    list_display_links = ("id",)
    search_fields = ("id", "Condition")
    list_filter = ("Number", "Topic")
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


class TopicsTasksAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = (
        "id",
        "Topic",
    )
    list_filter = ("question_id",)


admin.site.register(Questions)
admin.site.register(Topics, TopicsTasksAdmin)
admin.site.register(SourceTasks, SourceTasksAdmin)
admin.site.register(PrototypeTasks, PrototypeTasksAdmin)
admin.site.site_header = "TechnoSchool"
admin.site.site_title = "TechnoSchool"
admin.site.index_title = "TechnoSchool"
