from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'priority'
    )


admin.site.register(Task, TaskAdmin)
admin.site.site_header = 'Админпанель ToDo'