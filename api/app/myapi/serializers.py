# serializers.py
from rest_framework import serializers

from .models import Task
from .models import User

from django.contrib.auth.tokens import PasswordResetTokenGenerator

class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description')

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

    def validate(self, attrs):
        try:
            email = attrs.get('email', '')
            if User.objects.filter(email=email).exists():
                pass
            return attrs
        except expression as indentifier:
            pass
        return super().validate(attrs)