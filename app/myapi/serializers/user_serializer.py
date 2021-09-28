# serializers.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from rest_framework import serializers

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        # validated_data['username']
        user = UserModel.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'first_name', 'last_name',)

