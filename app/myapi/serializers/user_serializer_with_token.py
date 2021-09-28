# serializers.py
from rest_framework.exceptions import AuthenticationFailed
from django.utils.encoding import force_str
from rest_framework import serializers

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode

UserModel = get_user_model()

class UserSerializerWithToken(serializers.ModelSerializer):
    pass
