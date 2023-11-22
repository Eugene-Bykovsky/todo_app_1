from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    priority_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['name']

    def __str__(self):
        return self.name


class SubTask(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='subtasks')
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Подзадача'
        verbose_name_plural = 'Подзадачи'
        ordering = ['name']

    def __str__(self):
        return self.name
