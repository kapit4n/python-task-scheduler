from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class Task(models.Model):
    description = models.CharField(max_length=250)
    status = models.CharField(max_length=150, default='pending')
    priority = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    estimated_time = models.IntegerField(default=0)

    def __str__(self):
        return self.description
