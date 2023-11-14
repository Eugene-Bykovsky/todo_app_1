from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    priority_choices = [
        (1, 'Low'),
        (2, 'Medium'),
        (3, 'High')
    ]
    priority = models.CharField(max_length=10, choices=priority_choices)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['priority']

    def __str__(self):
        return self.name
