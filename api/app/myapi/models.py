from django.db import models

from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)


# Create your models here.

class Task(models.Model):
    description = models.CharField(max_length=250)
    def __str__(self):
        return self.description

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should  hace a Email')
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email= models.EmailField(max_length=255, unique=True, db_index=True)

    objects = UserManager()

    def __str_(self):
        return self.email



