from django.db import models
from datetime import datetime

from .task import Task

class TaskLog(models.Model):
    status = models.CharField(max_length=250, default='running')
    start_date = models.DateTimeField(default=datetime.now, blank=False)
    end_date = models.DateTimeField(default=datetime.now, blank=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='logs')

    class Meta:
        app_label = "myapi"


    def __str__(self):
        return self.status
