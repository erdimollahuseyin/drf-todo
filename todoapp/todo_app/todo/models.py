from django.db import models


class Task(models.Model):
    STATES = (('todo', 'To Do'), ('in progress', 'In Progress'), ('done', 'Done'))
    title = models.CharField(max_length=255, blank=False, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=4, choices=STATES, default='todo')
