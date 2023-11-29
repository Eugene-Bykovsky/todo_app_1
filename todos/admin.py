from django.contrib import admin

from .models import Task, SubTask


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'priority',
        'author'
    )


@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'body',
        'task',
        'completed'
    )


admin.site.site_header = 'Админпанель ToDo'
