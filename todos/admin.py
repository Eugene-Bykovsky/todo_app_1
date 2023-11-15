from django.contrib import admin

from .models import Task, SubTask


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'priority'
    )


class SubTaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'task',
        'completed'
    )


admin.site.register(Task, TaskAdmin)
admin.site.register(SubTask, SubTaskAdmin)
admin.site.site_header = 'Админпанель ToDo'