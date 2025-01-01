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



class SourceTasksAdmin(admin.ModelAdmin):
    list_display = ("id", "Number", "Topic", "Condition_for_students", "time_create", "time_update")
    list_display_links = ("id",)
    search_fields = ("id", "Condition")
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
    readonly_fields = ["time_create", "time_update"]
    empty_value_display = "-ничего-"
    list_per_page = 12
    form = TaskForm


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
    )
    readonly_fields = ["time_create", "time_update"]
    empty_value_display = "-ничего-"
    list_per_page = 12
    form = TaskForm


admin.site.register(Questions)
admin.site.register(Topics)
admin.site.register(PrototypeTasks, PrototypeTasksAdmin)
admin.site.register(SourceTasks, SourceTasksAdmin)
admin.site.register(Formulas)
admin.site.register(Limitations)
admin.site.register(PrototypeAnswers)
admin.site.register(SourceAnswers)
admin.site.site_title = "CyberStudy"
