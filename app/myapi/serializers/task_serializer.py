# serializers.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from rest_framework import serializers

from myapi.models import Task

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()

class TaskSerializer(serializers.ModelSerializer):

    logs = serializers.StringRelatedField(many=True, required=False,)

    class Meta:
        model = Task
        fields = ('id', 'description', 'status',
                  'priority', 'time', 'estimated_time', 'create_date', 'logs')

