from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)


class Task(models.Model):
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.description
