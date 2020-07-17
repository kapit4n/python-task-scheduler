# serializers.py
from rest_framework import serializers

from .models import Task

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class TaskSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Task
        fields = ('id', 'description')

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    class Meta:
        fields = ['email']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password','email', 'username', 'first_name', 'last_name',)

