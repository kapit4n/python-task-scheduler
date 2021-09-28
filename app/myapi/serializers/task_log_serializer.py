# serializers.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from rest_framework import serializers

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from myapi.models import TaskLog

class TaskLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskLog
        fields = ('id', 'status', 'task', 'start_date', 'end_date')
