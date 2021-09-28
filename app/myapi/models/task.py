from django.db import models
from datetime import datetime

class Task(models.Model):
    description = models.CharField(max_length=250, default='')
    status = models.CharField(max_length=150, default='pending')
    priority = models.IntegerField(default=0)
    create_date = models.DateTimeField(default=datetime.now, blank=False)
    update_date = models.DateTimeField(default=datetime.now, blank=True)
    time = models.IntegerField(default=0)
    estimated_time = models.IntegerField(default=0)


    class Meta:
        app_label = "myapi"

    def __str__(self):
        return self.description + ' ' + self.status + ' ' + str(self.pk)
