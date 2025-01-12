from django.contrib import admin

from apps.users.models import Users


class UsersAdmin(admin.ModelAdmin):
    """
    Кастомизация вкладки с пользователями в админ панели.
    """

    list_display = ("id", "username", "Class")
    list_display_links = ("id",)
    search_fields = ("id",)
    empty_value_display = "-ничего-"
    list_per_page = 20


admin.site.register(Users, UsersAdmin)
